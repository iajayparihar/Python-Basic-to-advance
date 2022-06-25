n=int(input("enter the no.=> "))
rev=0
while(n>0):
	r=n%10
	rev=rev*10+r
	n//=10

print("reverse no. is => ",rev)
	