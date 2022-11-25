import pandas as pd
import numpy as np
val=[100,200,300,400,500,50,40,30]
obj=pd.Series(val)

print(obj>=300)

print(obj[obj>=300])