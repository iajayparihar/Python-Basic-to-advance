n=int(input("enter the no. "))
k=0
i=2
while i<=n/2:
	if(n%i==0):
		k+=1
		break
	i+=1
if k==0:
	print("prime")
else:
	print("not prime")