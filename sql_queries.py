import sqlite3

# Generate a number correlation between each genre's sales, average rating, and number of reviews.
def genre_correlation(cursor):

    return cursor.execute('''
        WITH pre_process AS (
            SELECT DISTINCT
                s.title,
                s.platform,
                s.genre,
                s.global_sales
            FROM sales s
            JOIN metadata m ON s.title = m.title
        ),
        distinct_games AS (
            SELECT 
                title,
                genre,
                SUM(global_sales) AS total_sales
            FROM pre_process
            GROUP BY title
        ),
        ranked_games AS (
            SELECT 
                d.title,
                d.genre,
                d.total_sales,
                m.number_of_reviews,
                m.rating,
                ROW_NUMBER() OVER (PARTITION BY d.title ORDER BY m.rating DESC) AS rn
            FROM distinct_games d
            JOIN metadata m ON m.title = d.title
        ),
        add_rating AS (
            SELECT
                title,
                genre,
                total_sales,
                rating,
                number_of_reviews
            FROM ranked_games
            WHERE rn = 1
            ORDER BY title
        ),
        get_sales AS (
            SELECT
                genre,
                SUM(global_sales) AS total_sales
            FROM sales
            GROUP BY genre
        ),
        get_averages AS (
            SELECT 
                genre,
                SUM(total_sales) AS total_sales,
                ROUND(AVG(CAST(rating AS REAL)), 2) AS avg_rating,
                SUM(CAST(number_of_reviews AS INTEGER)) AS number_of_reviews
            FROM add_rating
            GROUP BY genre
        ),
        genre_stats AS (
            SELECT
                ga.genre,
                gs.total_sales,
                ga.avg_rating,
                ga.number_of_reviews
            FROM get_averages ga
            JOIN get_sales gs ON ga.genre = gs.genre
            ORDER BY gs.total_sales DESC
        )
        SELECT
            genre,
            ROUND(total_sales / NULLIF(number_of_reviews, 0), 3) AS sales_per_review
        FROM genre_stats
        LIMIT 6;                      
    ''')

# Identify each genre's sales, average rating, and number of reviews
def genre_comparisons(cursor):

    return cursor.execute('''
        WITH pre_process AS (
            SELECT DISTINCT
                s.title,
                s.platform,
                s.genre,
                s.global_sales
            FROM sales s
            JOIN metadata m ON s.title = m.title
        ),
        distinct_games AS (
            SELECT 
                title,
                genre,
                SUM(global_sales) AS total_sales
            FROM pre_process
            GROUP BY title
        ),
        ranked_games AS (
            SELECT 
                d.title,
                d.genre,
                d.total_sales,
                m.number_of_reviews,
                m.rating,
                ROW_NUMBER() OVER (PARTITION BY d.title ORDER BY m.rating DESC) AS rn
            FROM distinct_games d
            JOIN metadata m ON m.title = d.title
        ),
        add_rating AS (
            SELECT
                title,
                genre,
                total_sales,
                rating,
                number_of_reviews
            FROM ranked_games
            WHERE rn = 1
            ORDER BY title
        ),
        get_sales AS (
            SELECT
                genre,
                SUM(global_sales) AS total_sales
            FROM sales
            GROUP BY genre
        ),
        get_averages AS (
            SELECT 
                genre,
                SUM(total_sales) AS total_sales,
                ROUND(AVG(CAST(rating AS REAL)), 2) AS avg_rating,
                SUM(CAST(number_of_reviews AS INTEGER)) AS number_of_reviews
            FROM add_rating
            GROUP BY genre
        )
        SELECT
            ga.genre,
            gs.total_sales,
            ga.avg_rating,
            ga.number_of_reviews
        FROM get_averages ga
        JOIN get_sales gs ON ga.genre = gs.genre
        ORDER BY gs.total_sales DESC;                        
    ''')

# Identify the top-selling genre
def sales_by_genre(cursor):

    return cursor.execute('''
        SELECT 
            s.genre, 
            SUM(s.global_sales) AS total_sales
        FROM sales s
        GROUP BY s.genre
        ORDER BY total_sales DESC
        LIMIT 10;     
    ''')

# Extract games with high wishlist counts but low sales
def wishlist_analysis(cursor):

    return cursor.execute('''
        WITH MaxWishlist AS (
            SELECT 
                title,
                MAX(CAST(wishlist AS INTEGER)) AS wishlist_count
            FROM metadata
            GROUP BY title
        ),
        WishlistAnalysis AS (
            SELECT
                s.title,
                MAX(m.wishlist_count) AS wishlist_count,
                SUM(s.global_sales) AS global_sales
            FROM sales s
            JOIN MaxWishlist m ON s.title = m.title
            GROUP BY s.title
        )
        SELECT
            title,
            wishlist_count,
            global_sales
        FROM WishlistAnalysis
        ORDER BY wishlist_count DESC, global_sales ASC
        LIMIT 10;
    ''')

# Compare the relationship between total games released and total sales by publisher
def games_to_sales_ratio(cursor):

    return cursor.execute('''
        SELECT 
            publisher, 
            COUNT(*) AS games_count,
            SUM(global_sales) AS total_sales
        FROM sales
        GROUP BY publisher
        ORDER BY total_sales DESC
        LIMIT 10;              
    ''')

# Find the top 10 selling games
def top_ten(cursor):

    top_ten = cursor.execute('''
        SELECT 
            title, 
            SUM(global_sales) AS total_sales
        FROM 
            sales
        GROUP BY
            title
        ORDER BY 
            total_sales DESC
        LIMIT 10;
    ''')
    print("\nTop 10 Selling Games:"); print()
    for row in top_ten:
        print(row)
