import pandas as pd
import numpy as np
df=pd.read_csv("./dataset.csv") #this will convert csv to dataframes


# Fill missing Category with 'Unknown'
df['Category'] = df['Category'].fillna('Unknown')

# Fill missing Quantity with the median quantity value
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# Ensure Date is recognized as a datetime data type
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Total Spend per transaction
df['Total_Revenue'] = df['Quantity'] * df['Price_Per_Unit']

# Extract day of the week
df['Day_of_Week'] = df['Date'].dt.day_name()

print(df)
