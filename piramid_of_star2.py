m=1
for i in range(1,6):
	for k in range(1,7-i):
		print("",end=" ")
	for j in range(1,i+m):
		if(j==1 or j==(i+m-1)):
			print("*",end="")
		else:
			print(" ",end="")
	m+=1
	print()
m-=2
for i in range(4,0,-1):
	for k in range(1,7-i):
		print("",end=" ")
	for j in range(1,i+m):
		if(j==1 or j==(i+m-1)):
			print("*",end="")
		else:
			print(" ",end="")
	m-=1
	print()
