n=int(input("enter the number ="))
i=n
a=0
for i in range(2,n):
	if(n/i==i):
		a=i
		break
if(a==i or n==1):
	print("Perfect square",i)
else:
	print("nooo")
