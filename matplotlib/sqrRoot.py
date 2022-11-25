import matplotlib.pyplot as pl 
import numpy as np

fib=[0,1,1,2,3,5,8,13,21,34]
srfib=np.sqrt(fib)
print(srfib)

pl.figure(figsize=(10,7),facecolor="m")
pl.grid()
# pl.plot(range(1,11),fib,range(1,11),srfib,marker="o",markersize=6,markeredgecolor="k",linestyle="dashed",) #auto take different colors

pl.plot(range(1,11),fib,"c+",markersize=10,markeredgecolor="k",linewidth=2,linestyle="dotted")
pl.plot(range(1,11),srfib,"r8",linewidth=2,linestyle="solid")

pl.show()