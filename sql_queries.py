import sqlite3

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
