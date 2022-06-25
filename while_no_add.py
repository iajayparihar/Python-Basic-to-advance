n=int(input("enter the no.=> "))
r=0
add=0
while(n>0):
	r=n%10
	add=add+r
	n//=10
print("The addition of all no. is=>",add)