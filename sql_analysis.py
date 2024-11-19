import sqlite3

# Connect to the database
db = './videogames.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

# Find the top 10 selling games
top_ten = cursor.execute('''
    SELECT 
        title, 
        sales_number 
    FROM 
        sales
    ORDER BY 
        sales_number
    LIMIT 10;
''')
for row in top_ten:
    print(row)

