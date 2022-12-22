import matplotlib.pyplot as pl
import numpy as np
val=[[5,25,45,20],[4,23,49,17],[6,22,47,19]]
x=np.arange(4)
y=range(4)
print((x))
print((y))
pl.bar(x+0.0, val[0],color="b",width=0.25)
pl.bar(x+0.25, val[1],color="g",width=0.25)
pl.bar(x+0.50, val[2],color="r",width=0.25)

pl.show()