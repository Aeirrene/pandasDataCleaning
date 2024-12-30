# data_cleaning.py
def clean_data(df):
    """
    Cleans the input DataFrame by:
    1. Removing missing values
    2. Converting 'Age' to integers
    3. Removing duplicate rows
    """
    # Remove missing values
    df = df.dropna()

    # Convert 'Age' column to integer
    if 'Age' in df.columns:
        df['Age'] = df['Age'].astype(int)

    # Remove duplicates
    df = df.drop_duplicates()

    return df
