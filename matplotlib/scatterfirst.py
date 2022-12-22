import matplotlib.pyplot as pl
import numpy as np
arr1=np.linspace(-1, 1,5)
arr2=np.exp(arr1)
colarr=['r','g','b','k','m']
sarr=[20,40,60,80,100]
pl.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# pl.scatter(arr1,arr2,marker,size,color)
pl.scatter(arr1,arr2,marker="x",s=sarr,c=colarr)
pl.show()