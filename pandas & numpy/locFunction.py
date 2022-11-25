import pandas as pd 
dict={"A":[9,8,7,5,2],
        'B':[7.4,1.2,4.4,8.8,5.5],
        'C':[90,91,92,93,94],
        'D':[1,2,3,4,5]}
mks=pd.DataFrame(dict,index=["Acc",'Eco','Eng','Ip','Maths'])
print(mks)
mks.loc['Comp',:]=22
print(mks)
mks.loc['HIndi',:]=[2,5,3,5]
print(mks)
print("------------------------1")

mks.A["Acc"]=444
print(mks)

print("------------------------2")

mks.loc['Acc','B']=123
print(mks)

print("------drop--row----------------3")

print(mks.drop(['Acc'],axis=0))

print("-------drop column-------------4")

print(mks.drop(['A','D'],axis=1))

print("-----------------------5")
# print(mks.drop([range(1)]))   this is only for numeric column

