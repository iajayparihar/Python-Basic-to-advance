import pandas as pd
sales1={"year1":{"Q1":300,"Q2":500,"Q3":600},
        "year2":{"Q1":123,"Q2":456,"Q3":789},
        "year3":{"Q1":333,"Q2":222,"Q3":111}
    }
sales2={"year1":{"Q1":3000,"Q2":5000,"Q3":6000},
        "year2":{"Q1":13,"Q2":456,"Q3":79},
        "year3":{"Q1":333,"Q2":22,"Q3":111}
    }

df1=pd.DataFrame(sales1)
df2=pd.DataFrame(sales2)
print(df1)
print("----------------")
print(df2)
print("----df3=df1+df2------")

df3=df1+df2
print(df3)
print("-------sub---------")
df4=df1.sub(df2)
print(df4)
print("------rsub----------")
df4=df1.rsub(df2)
print(df4)