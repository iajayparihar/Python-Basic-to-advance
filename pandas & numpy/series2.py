import pandas as pd
import numpy as np
obj=pd.Series({"jan":31,"feb":28,"mar":31})
print(obj)

print("------------------------------------")

data1=[12,45,78]
arr=["jan","feb","mar"]
obj=pd.Series(index=arr,data=data1)
print(obj)

print("------------------------------------")

data1=[12,45,78,96]
arr=np.arange(9,13)
obj=pd.Series(index=range(1,8,2),data=data1)
print(obj)

print("------------------------------------")

arr=["A","B","C","D","E"]
val=[1000,2000,3000,4000,np.NAN]
obj=pd.Series(data=val,index=arr,dtype=np.float64)
print(obj)