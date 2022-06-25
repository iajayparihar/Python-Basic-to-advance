for i in range(5,0,-1):
	for j in range(1,7-i):
		print(" ",end="")
	for k in range(1,6):
		if(i==1 or i==5 or k==1 or k==5):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()