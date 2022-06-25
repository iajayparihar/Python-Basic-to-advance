def fact(x):
	y=1
	while(x>0):
		y=y*x
		x-=1
	return y
n=int(input("Enter the no. ="))
m=fact(n)
print(m)