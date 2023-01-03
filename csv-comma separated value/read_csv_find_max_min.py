import pandas as pd
df=pd.read_csv("student1.csv",index_col="roll no")
print(df)
print("maximum marks is:- ",df.marks.max())
print("minimum marks is:- ",df.marks.min())