import os
import sqlite3

db_file_path = './videogames.db'

# Connect to the database
def connect_to_db(db):

    if not os.path.exists(db):
        print(f"Database '{db}' does not exist.")
        return None
        
    return sqlite3.connect(db)

conn = connect_to_db(db_file_path)
cursor = conn.cursor()

## ======================================================================== ##

# Find the top 10 selling games
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

# Average sales for each genre
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
