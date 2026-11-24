import pandas as pd

df=pd.DataFrame({
    "name": ["jason","lucia","perman"],
    "rollno": [127,None,2]
 })
print(df)
df=df.fillna(5)
print(df.columns)
print(df.values)
print(df)