r=0
for n in range(1,101):
	rev=0
	while(n>0):
		r=n%10
		rev=rev*10+r
		n//=10
	print(rev)