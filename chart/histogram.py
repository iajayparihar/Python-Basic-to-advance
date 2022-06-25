import matplotlib.pyplot as plt
ages =[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40,1,1]
range=(0,100)
bin=20
plt.hist(ages,bin,range,color="green",histtype='bar',rwidth=0.9)
plt.xlabel("age")
plt.ylabel("no.of people")
plt.title("my histogram!")
plt.show()
