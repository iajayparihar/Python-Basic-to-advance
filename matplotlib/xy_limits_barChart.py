import matplotlib.pyplot as pl
import numpy as np
a=np.arange(4)
y=[5,25,45,20]
pl.xlim(-2,4)
pl.ylim(0,60)
pl.bar(a, y)    
pl.show()