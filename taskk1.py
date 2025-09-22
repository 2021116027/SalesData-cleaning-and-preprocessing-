import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\ss041\Downloads\archive (2)\retail_store_sales.csv")
print(df)
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
df.columns=df.columns.str.title().str.replace(' ','_')
print(df)
# 1. Handle missing values in numeric columns
numeric_columns = ['Price_Per_Unit', 'Quantity', 'Total_Spent']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  
    df[col] = df[col].fillna(df[col].mean())  

# 2. Handle missing values in categorical columns
categorical_columns = ['Item', 'Payment_Method', 'Discount_Applied']
for col in categorical_columns:
    if col == 'Discount_Applied':
        df[col] = df[col].fillna('False')  
    else:
        df[col] = df[col].fillna('Unknown')  

# 3. Convert date column to datetime format
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], errors='coerce')

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Handle inconsistent text data (convert to proper case)
text_columns = ['Category', 'Item', 'Payment_Method', 'Location']
for col in text_columns:
    df[col] = df[col].astype(str).str.title()

# 6. Convert Discount Applied to boolean
df['Discount_Applied'] = df['Discount_Applied'].astype(str).str.title().replace({
    'True': True, 'False': False, 'Nan': False
})

# 7. Remove rows with invalid dates (if any)
df = df.dropna(subset=['Transaction_Date'])

# 8. Reset index after cleaning
df = df.reset_index(drop=True)

# Display cleaning results
print("\nAfter cleaning:")
print("Dataset shape:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nData types:")
print(df.dtypes)
print("\nFirst few rows after cleaning:")
print(df.head())

# Save cleaned dataset
df.to_csv('retail_store_sales_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'retail_store_sales_cleaned.csv'")

