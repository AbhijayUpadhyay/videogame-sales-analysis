import pandas as pd
import sqlite3

sales = './LargestCleanedDS.csv'
metadata = './games.csv'

# Convert csv files to DataFrames
df_sales = pd.read_csv(sales)
df_metadata = pd.read_csv(metadata)

# Strip excess whitespace from column names and rows
df_sales.columns = df_sales.columns.str.strip()
df_metadata.columns = df_metadata.columns.str.strip()

df_metadata = df_metadata.drop(df_metadata.columns[0], axis=1)

df_sales = df_sales.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df_metadata = df_metadata.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Connect to the database
db = 'videogames.db'
conn = sqlite3.connect(db)

# Add tables to the database
df_sales.to_sql('sales', conn, if_exists='replace', index=False)
df_metadata.to_sql('metadata', conn, if_exists='replace', index=False)

conn.close()
