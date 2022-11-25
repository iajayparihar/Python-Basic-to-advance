import pandas as pd
import numpy as np
val1=["Abhi","ajay","venom","chintu","abhigyan","vij","pta nhi "]
val2=["bangu","limayra","kimayra","nanu","bendi"]
obj1=pd.Series(val1)
obj2=pd.Series(val2)
print(obj1)
print(obj2)

print(obj1+obj2) # if obj1 and obj2 contain strings then they concatinate

val1=[10,20,30,40,50]
val2=[1,2,3,4]
obj1=pd.Series(val1)
obj2=pd.Series(val2)
print(obj1)
print(obj2)

# value + NaN = Nan

print(obj1+obj2) # if obj1 and obj2 contain intergers then there value added by index
