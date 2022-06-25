def power(x,y):
	if y==1:
		return (x)
	else:
		return(x*power(x,y-1))
#-- main--
m=int(input("enter the value of M="))
n=int(input("enter the value of N="))
print("Answer=",power(m,n))