import pandas as pd
import numpy as np
df=pd.read_csv("./dataset.csv") #this will convert csv to dataframes

# Check how many values are missing per column
print(df.isna().sum())

# Fill missing Category with 'Unknown'
df['Category'] = df['Category'].fillna('Unknown')

# Fill missing Quantity with the median quantity value
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

print(df)
