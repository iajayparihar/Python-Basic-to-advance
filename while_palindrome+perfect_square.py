n=1
i=1001
j=1
sq=4
while(n<i):
	rev=0
	while(n==j*j):
		sq=n
		while(sq>0):
			r=sq%10
			rev=rev*10+r
			sq//=10
		if(n==rev):
			print("Palindrome + Perfect square",n)
		else:
			pass
		j+=1
	
		
	n+=1


