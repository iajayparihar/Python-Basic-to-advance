print("fibonacci series")

n=int(input("How many no. you want to print:- "))
f1=-1
f2=1
for i in range(n):
	f=f1+f2
	print(f)
	f1=f2
	f2=f
	