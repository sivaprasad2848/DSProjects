import pandas as pd
import numpy as np
df=pd.read_csv("./dataset.csv") #this will convert csv to dataframes
#print(df)
print(df.info()) #check the structure and datatypes
print(df.describe())#Summary Statistics of numberic column

