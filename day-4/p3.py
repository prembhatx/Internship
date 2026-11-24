import pandas as pd

df=pd.read_csv("tested.csv")
print(df)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
print(df.min())
print(df.axes)
