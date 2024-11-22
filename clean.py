import pandas as pd

def handle_null_values(df):

    # Drop rows with NULL values    
    df = df.dropna()
    
    # Drop columns with headers that are null or contain no letters/numbers
    df = df[[col for col in df.columns if col and any(c.isalnum() for c in str(col))]]

    return df

def process_dataframe(df):

    # Check if the input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input must be a pandas DataFrame.")
    
    df = handle_null_values(df)

    # Strip excess whitespace and new lines
    df.columns = df.columns.str.strip()
    df = df.map(lambda x: x.replace("\n", "").strip() if isinstance(x, str) else x)

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace spaces with underscores in column headers
    df.columns = df.columns.str.replace(' ', '_')

    # File-specific adjustments    
    df.columns = df.columns.str.replace('name', 'title')
    if df.columns[0] == 'rank':
        df.drop('rank', axis=1, inplace=True)

    if df.columns[2] == 'year':
        df['year'] = pd.to_datetime(df['year'], format='%Y')

    return df