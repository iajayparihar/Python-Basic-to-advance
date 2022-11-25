import pandas as pd
import numpy as np
arr=["A","B","C","D","E"]
val=[1000,2000,3000,4000,np.NAN]
obj=pd.Series(data=val,index=arr,dtype=np.float64)
print(obj)
print("Index =",obj.index)
print("values =",obj.values)
print("size =",obj.size)
print("dimentions =",obj.ndim)
# The shape property returns a tuple containing the shape of the DataFrame.
# The shape is the number of rows and columns of the DataFrame
print("shape =",obj.shape)
print("bytes =",obj.nbytes)
print("Nan values =",obj.hasnans)
print("value is empty =",obj.empty)