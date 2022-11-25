import pandas as pd
import numpy as np
val=["Abhi","ajay","venom","chintu","abhigyan"]
ind=[1,2,3,4,5]
obj1=pd.Series(val,ind)
print(obj1)

obj2=obj1.reindex([4,5,3,2,1])
print(obj2)
