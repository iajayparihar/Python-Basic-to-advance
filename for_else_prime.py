n=int(input("Enter the no.=> "))
for i in range(2,n):
	if(n%i==0):
		print("no. is not prime")
		break
else:
	print("prime no.")