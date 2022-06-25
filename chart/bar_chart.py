import matplotlib.pyplot as plt
left=[1,2,3,4,5]
height=[10,24,36,40,35]
t_lable=['one',"two","three","four","five"]
plt.bar(left,height,tick_label=t_lable,width=0.6,color=["red","blue"])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim(1,10)
plt.ylim(1,60)
plt.title("my bar Chart!")
plt.show()