# main.py
from data_cleaning import clean_data
from data_transformation import transform_data
import pandas as pd

# Example dataset
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}

# Load data
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Clean data
df = clean_data(df)
print("Cleaned Data:")
print(df)

# Transform data
grouped_df, pivoted_df = transform_data(df)
print("Grouped Data:")
print(grouped_df)
print("Pivoted Data:")
print(pivoted_df)
