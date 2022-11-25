import matplotlib.pyplot as pl

# plot(x,y,"line-color ")  ==> only line show

# plot(x,y,"line-color + marker") ==> only marker points show
# plot(x,y,"line-color : marker") ==> line and marker  show




x=[1,2,3,4,5]
y=[1,4,6,8,10]
pl.figure(figsize=(4,5),facecolor="red")
# pl.plot(x,y,"y+")
pl.plot(x,y,"k",marker="X",markeredgecolor="y",markersize=10)
pl.show()