import matplotlib.pyplot as pl 
contri=[17,8.8,12.7,14]
houses=["vidya","kshma","kalam","ram"]
myclr=['r','g','b','m']
explo=[0,0.2,0,0.3]

pl.pie(contri,colors=myclr,labels=houses,explode=explo,autopct="%4.2d",shadow=True)
pl.title("contribution of houses")
pl.show()