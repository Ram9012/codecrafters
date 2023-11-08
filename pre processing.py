'''
df = pd.read_csv('recession.csv')
df_cleaned = df.dropna()
df_cleaned.to_csv('cleaned_recession.csv', index=False)
'''

'''
df = pd.read_csv('recession.csv')
missing_values = df.isnull()
missing_count = missing_values.sum()
df_cleaned = df.dropna()
df['Percentage'].fillna(df['column_name'].mean(), inplace=True)
df['column_name_missing'] = df['column_name'].isnull().astype(int)
df.to_csv('recession_data1.csv', index=False)
'''

'''
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('filled_data.csv')

# Check for missing values (NaN)
missing_values = df.isnull().sum()

# Check for data format issues or other inconsistencies
# You may want to add additional checks depending on your specific requirements

# Display the results
print("Missing values (NaN):")
print(missing_values)

# Optionally, you can check for other issues and inconsistencies in your data here

# Example: Checking for duplicates
duplicate_rows = df[df.duplicated()]
if not duplicate_rows.empty:
    print("\nDuplicate rows:")
    print(duplicate_rows)

# Example: Checking for data type issues
# You can use df.dtypes to inspect the data types of columns and look for inconsistencies
data_types = df.dtypes
print("\nData types:")
print(data_types)
'''

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('recession.csv')

# Iterate through the columns and fill missing values with column means
for col in df.columns:
    if df[col].dtype in [int, float]:
        col_mean = df[col].mean()
        df[col].fillna(col_mean, inplace=True)

# Save the filled DataFrame back to a CSV file
df.to_csv('filled_data.csv', index=False, sep=',')

# Display the DataFrame with missing values filled
print(df)


