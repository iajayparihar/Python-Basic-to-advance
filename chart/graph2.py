import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[2,4,1,5,2,6]
plt.plot(x,y,color="green",linestyle="dashed", linewidth=2,marker="o",markerfacecolor="red")
plt.xlim(1,8)
plt.ylim(1,8)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("some customizations!")
plt.legend()
plt.show()
