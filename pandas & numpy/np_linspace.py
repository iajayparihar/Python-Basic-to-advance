import pandas as pd
import numpy as np

obj=pd.Series(np.linspace(10,100,7) , index=(x for x in range(1,8)))
print(obj)