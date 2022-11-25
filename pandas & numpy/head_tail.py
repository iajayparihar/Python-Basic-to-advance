import pandas as pd
import numpy as np
val=["Abhi","ajay","venom","chintu","abhigyan","vij","pta nhi "]
obj=pd.Series(val,index=(x for x in range(1,len(val)+1)))
print(obj)
print(obj.head()) # head method only showes "upper" 5 row
print(obj.tail()) # tail method only show "bottom" 5 row

print(obj.head(2))
print(obj.tail(2))