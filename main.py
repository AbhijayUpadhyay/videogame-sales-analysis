# main.py controls the workflow. This file will import and call functions from other modules.
# As we progress through main.py we will learn more about our datasets.

import os
import pandas as pd
from clean import process_dataframe
from create_db import create_database
from sql_analysis import run_sql_queries
# from analysis import analyze_data

def main():

    # Step 1: Load the datasets
    sales = './vgsales.csv'
    metadata = './games.csv'

    # Step 2: Convert csv files to DataFrames
    def read_csv_file(file_path):

        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist.")
            return None
        
        df = pd.read_csv(file_path)
        return df

    df_sales = read_csv_file(sales)
    df_metadata = read_csv_file(metadata)

    # Step 3: Clean the data
    df_sales = process_dataframe(df_sales)
    df_metadata = process_dataframe(df_metadata)

    # Step 4: Create SQL database
    db_file_path = create_database(df_sales, df_metadata)

    # Now we can begin to find patterns in video game sales...
    # Step 5: Run SQL analysis
    run_sql_queries(db_file_path)    # <-- Comment out function call to skip query results

    # Next steps: DataFrame analysis / Predictions
    
    

if __name__ == '__main__':
    main()
