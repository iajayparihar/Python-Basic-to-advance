m=1
for i in range(1,6):
	for k in range(1,7-i):
		print("",end=" ")
	for j in range(1,i+m):
		if(j==1 or j==(i+m-1) or i==5 ):
			print("*",end="")
		else:
			print(" ",end="")
	m+=1
	print()