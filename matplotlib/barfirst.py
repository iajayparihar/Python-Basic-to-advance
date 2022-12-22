import matplotlib.pyplot as pl
import numpy as np
a=[1,2,3,4,7]
b=[2,4,6,8,7]
# pl.bar(a,b,width=[.5,.9,.3,.6,.5],color=['r','g','b','k','m'])
pl.barh(a,b,color=['r','g','b','k','m'])
pl.show()