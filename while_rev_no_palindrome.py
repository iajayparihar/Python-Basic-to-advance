n=int(input("enter the no.=> "))
a=n
rev=0
while(n>0):
	r=n%10
	rev=rev*10+r
	n//=10

if(a==rev):
	print("the given no. is palindrome",a)
else:
	print("given no. is not palindrome",a)
print("reverse no. is => ",rev)

