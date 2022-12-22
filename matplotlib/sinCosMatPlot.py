import matplotlib.pyplot as pl
import numpy as np
x=np.arange(0,10,.1)
a=np.cos(x)
b=np.sin(x)
pl.plot(x,a,"r")
pl.xlabel("xlabel")
pl.ylabel("y label")
pl.plot(x,b,"g")

pl.show()