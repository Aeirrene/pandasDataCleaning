# data_transformation.py
def transform_data(df):
    """
    Transforms the input DataFrame by:
    1. Grouping by 'Country' and calculating the mean 'Age'
    2. Pivoting the DataFrame with 'Country' as index and 'Age' as values
    """
    # Group by 'Country' and calculate the mean 'Age'
    grouped_df = df.groupby('Country')['Age'].mean()

    # Pivot the DataFrame
    pivoted_df = df.pivot_table(index='Country', values='Age', aggfunc='mean')

    return grouped_df, pivoted_df
