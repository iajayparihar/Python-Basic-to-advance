import pandas as pd
import numpy as np
val=["Abhi","ajay","venom","chintu","abhigyan","vij","pta nhi "]
obj=pd.Series(val)
print(obj)
print(obj.drop(0)) # only drop from screen

obj.drop(6,inplace=True) # remove from data base 
print(obj)
