import matplotlib.pyplot as plt
activities=["eat","sleep","work","play"]
slice=(3,8,8,6)
color=['r','y','g','b']
plt.pie(slice,labels=activities,colors=color,startangle=90,shadow=True,explode=(0,0,0.3,0),radius=1.2,autopct="%0.2f%%")
plt.show()