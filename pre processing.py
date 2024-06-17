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
df = pd.read_csv('filled_data.csv')
missing_values = df.isnull().sum()

print("Missing values (NaN):")
print(missing_values)

duplicate_rows = df[df.duplicated()]
if not duplicate_rows.empty:
    print("\nDuplicate rows:")
    print(duplicate_rows)

data_types = df.dtypes
print("\nData types:")
print(data_types)
'''

import pandas as pd
df = pd.read_csv('recession.csv')

for col in df.columns:
    if df[col].dtype in [int, float]:
        col_mean = df[col].mean()
        df[col].fillna(col_mean, inplace=True)

df.to_csv('filled_data.csv', index=False, sep=',')
print(df)


