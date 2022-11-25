import pandas as pd
dict1={'studid':[1,2,3,4],
        'studname':['aj','vij','mmat','kalu']}
dict2={'studid':[4,5,6,7],
        'studname':['ajay','vijay','mamat','kali']}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)

df3=pd.concat([df1,df2])
df4=pd.concat([df1,df2],ignore_index=True)
df5=pd.concat([df1,df2],axis=1,ignore_index=True)
print(df1)
print(df2)
print(df3)
print(df4)
print(df5)