import os
import sqlite3

# Average sales for each genre
def avg_sales_genre(cursor):

    avg_sales = cursor.execute('''
        SELECT 
            m.genres, 
            AVG(s.sales_number) AS avg_sales
        FROM 
            sales s
        JOIN 
            metadata m
        ON 
            s.title = m.title
        GROUP BY 
            m.genres
        ORDER BY 
            avg_sales DESC;               
    ''')
    for row in avg_sales:
        print(row)

# Find the top 10 selling games
def top_ten(cursor):

    top_ten = cursor.execute('''
        SELECT 
            title, 
            sales_number 
        FROM 
            sales
        ORDER BY 
            sales_number DESC
        LIMIT 10;
    ''')
    for row in top_ten:
        print(row)


def run_sql_queries(db):

    # Connect to the database
    def connect_to_db(db):

        if not os.path.exists(db):
            print(f"Database '{db}' does not exist.")
            return None
            
        return sqlite3.connect(db)

    conn = connect_to_db(db)
    cursor = conn.cursor()

    ## ======================================================================== ##

    # Find the top 10 selling games
    top_ten(cursor)

    # Average sales for each genre
    avg_sales_genre(cursor)
