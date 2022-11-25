import pandas as pd
import numpy as np

np1=np.arange(1,6)
obj1=pd.Series(x for x in range(50,55))
print(obj1)
obj1=pd.Series(np1)
print(obj1)