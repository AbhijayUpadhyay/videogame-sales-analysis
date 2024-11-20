import pandas as pd

def process_dataframe(df):

    # Check if the input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input must be a pandas DataFrame.")

    # Drop rows with NULL values    
    df = df.dropna()

    # Strip excess whitespace and new lines
    df.columns = df.columns.str.strip()

    df = df.map(lambda x: x.replace("\n", "").strip() if isinstance(x, str) else x)


    # Remove unnamed columns
    df = df.loc[:, df.columns.notnull() & (df.columns != "")]

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace spaces with underscores
    df.columns = df.columns.str.replace(' ', '_')

    return df