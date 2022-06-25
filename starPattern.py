a=5
for i in range(1,5):
	b=1
	for j in range(1,i+a):
		if (i==1 or i==b or j==a ):
			print('*',end=" ")
		else:
			print(" ",end=" ")
		b+=1
	a+=1	
	print()