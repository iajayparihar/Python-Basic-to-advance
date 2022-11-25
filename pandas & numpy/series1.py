import pandas as pd
# Series mrthod contain data and index
#     .series(data,index)
obj=pd.Series([1,2,3,4],index=["a","b","c","d"])
print(obj)
print("--------------------------------------------------")
obj.index.name="my index"
print(obj)
print("--------------------------------------------------")
obj.name="my value"
print(obj)

