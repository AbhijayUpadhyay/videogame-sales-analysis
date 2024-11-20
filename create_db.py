import pandas as pd
import os
import sqlite3
import clean

sales = './LargestCleanedDS.csv'
metadata = './games.csv'

## ======================================================================== ##

# Convert csv files to DataFrames
def read_csv_file(file_path):

    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return None
    
    df = pd.read_csv(file_path)
    return df

df_sales = read_csv_file(sales)
df_metadata = read_csv_file(metadata)

## ======================================================================== ##

# Clean and format the dataframes
df_sales = clean.process_dataframe(df_sales)
df_metadata = clean.process_dataframe(df_metadata)

## ======================================================================== ##

# Connect to the database
db = 'videogames.db'
conn = sqlite3.connect(db)

# Add tables to the database
df_sales.to_sql('sales', conn, if_exists='replace', index=False)
df_metadata.to_sql('metadata', conn, if_exists='replace', index=False)

conn.close()
