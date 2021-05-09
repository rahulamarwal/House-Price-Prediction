import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize']=(20,10)
import functions

## Fetching Data
dataset = pd.read_csv('Bengaluru_House_Data.csv')

## -------- Data Cleaning ----------
df = dataset.drop(['area_type','availability','society','balcony'],axis=1)
df = df.dropna()
df['BHK'] = df['size'].apply(lambda x : int(x.split()[0]))
df.drop('size',axis=1,inplace=True)
df = df[~df['total_sqft'].apply(functions.is_float)]
print(df.head())
