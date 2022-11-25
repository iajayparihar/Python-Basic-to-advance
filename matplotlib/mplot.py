import matplotlib.pyplot as pl
a=[2,3,5,6]
b=[4,6,10,12]
pl.plot(a,b,"g")

x=[1,3,5,8]
y=[2,7,8,12]
pl.plot(x,y,"r",linestyle="dotted",linewidth=3)
pl.xlabel("x side")
pl.ylabel("y side")
pl.show()