import sqlite3

def create_database(df_sales, df_metadata):

    # Connect to the database
    db = 'videogames.db'
    conn = sqlite3.connect(db)

    # Add tables to the database
    df_sales.to_sql('sales', conn, if_exists='replace', index=False)
    df_metadata.to_sql('metadata', conn, if_exists='replace', index=False)

    conn.close()
    return db
