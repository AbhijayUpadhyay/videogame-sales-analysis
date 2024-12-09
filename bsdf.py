# Code to find the best selling games every year
# bsdf is short for best selling dataframe (a dataframe of the best selling games)
import sqlite3
import sql_queries
import pandas as pd

def best_selling(db):
    conn = sqlite3.connect(db)
    # sqlite3.connect(db)
    cursor = conn.cursor()

    query = cursor.execute('''
    SELECT title, year, global_sales, genre
    FROM sales AS s1 
    WHERE global_sales = (SELECT MAX(global_sales) FROM sales AS s2 WHERE s1.year = s2.year)
    ORDER BY year''')

    result = cursor.fetchall()

    rows = result
    bestSellersDf = pd.DataFrame(rows, columns=['title', 'year', 'global_sales', 'genre'])
    bestSellersDf

    conn.close()

    return bestSellersDf