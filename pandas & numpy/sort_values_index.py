import pandas as pd
import numpy as np
val=[45,12,52,1,48,98,75,62,32]

obj1=pd.Series(val)
print(obj1)
print(obj1.sort_values())
print(obj1.sort_values(ascending=False))

print(obj1.sort_index())
print(obj1.sort_index(ascending=False))
