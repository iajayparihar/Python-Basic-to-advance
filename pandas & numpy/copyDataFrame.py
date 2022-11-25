import pandas as pd
dict={"A":[9,8,7,5,2],
        'B':[7.4,1.2,4.4,8.8,5.5],
        'C':[90,91,92,93,94],
        'D':[1,2,3,4,5]}
mks1=pd.DataFrame(dict,index=(x for x in range(1,6)))
print("-------mks 1-------------")
print(mks1)
mks2=mks1
print("-------mks 2-------------")
mks2=pd.DataFrame(mks1,copy=True)
print(mks2)

print("-------mks 2.A[0]=23-------------")
mks2.A[1]=23
print(mks2)
print(mks1)


