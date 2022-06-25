import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[1,2,3,4,5,6,7,8]
plt.scatter(x, y,marker="*",s=30, label="star",color="red")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.title("my SCATTER plot!")
plt.show()
