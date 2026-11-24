import pandas as pd

df=pd.DataFrame({

"shubhchintak":["ash","prem","akash","viral","Tanush"],
"roll_num":[1,2,3,4,5],
"course":["BBA","BCA","MCOM","BCOM","PHARMACY"]

})
print(df)
df=df.fillna(10)
print(df)
print(df.columns)
print(df.values)
print(df.min())
