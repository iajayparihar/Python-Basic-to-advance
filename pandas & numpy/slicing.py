import pandas as pd
import numpy as np
arr=["A","B","C","D","E"]
val=[1000,2000,3000,4000,np.NAN]
obj=pd.Series(data=val,index=arr,dtype=np.float64)
print(obj[0])
print("---------------------------------------")
print(obj["A"]) #case sensitive A and a are different
print("---------------------------------------")

print(obj[1:])
print("---------------------------------------")
print(obj[:3])
print("---------------------------------------")
print(obj[::2])
print("---------------------------------------")