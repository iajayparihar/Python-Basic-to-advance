import pandas as pd 
dict={'A':[9,2,5,4,7],"B":[7.4,1.2,5.5,8.8,1.6],
        'C':[90,24,55,46,78],"D":[73.4,21.2,25.53,84.8,12.6]
        }
mks1=pd.DataFrame(dict,index=(x for x in range(1,6)))
print(mks1)
print("------")
# column min
print(mks1.min())
print("------")
# row min
print(mks1.min(axis=1,skipna=True,numeric_only=True))
print("-----------------------------")

print(mks1.max())
print("-----------------")
print(mks1.max(axis=1,skipna=True,numeric_only=True))
print("-----------------")
print(mks1.mode())
print("-----------------")
print(mks1.mode(axis=1,numeric_only=True))
print("-----------------")
print(mks1.mean())
print("-----------------")
print(mks1.mean(axis=1,skipna=True,numeric_only=True))
print("-----------------")
print(mks1.median())
print("-----------------")
print(mks1.median(axis=1,skipna=True,numeric_only=True))
print("-----------------")



print(mks1.sum())
print(mks1.sum(axis=1,numeric_only=None,skipna=True))
print(mks1.loc[:,"A"].sum())
print(mks1.loc[1:2,:].sum())
print(mks1.iloc[:,1].sum())
print(mks1.iloc[0:1,:].sum())
