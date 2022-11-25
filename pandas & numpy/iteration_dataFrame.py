import pandas as pd
sales={"year1":{"Q1":3000,"Q2":5000,"Q3":6000},
        "year2":{"Q1":123,"Q2":456,"Q3":789},
        "year3":{"Q1":333,"Q2":222,"Q3":111}
    }
df=pd.DataFrame(sales,)
print(df)
for (row,rseries) in df.iterrows():
    print("----------")
    print('row index',row)
    print('Conrainning')
    print(rseries)

print("++++++++++++++++++++++++")

for (col,cseries) in df.iteritems():
    print("----------")
    print('col index',col)
    print('Conrainning')
    print(cseries)