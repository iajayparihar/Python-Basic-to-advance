n=int(input("Enter the no. "))
i=0
while i<n:
	if(i%7==0)and(not(i%3==0)):
		print(i)
	i=i+1
	