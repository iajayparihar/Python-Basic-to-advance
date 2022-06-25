n=int(input("Enter the piramid of no. hight="))
for i in range(1,n+1):
	for k in range(1,n+1-i):
		print("",end=" ")
	for j in range(1,i+1):
		print("*",end=" ")
	print()