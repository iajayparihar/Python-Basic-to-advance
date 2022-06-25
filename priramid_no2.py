for i in range(1,6):
	m=i
	for a in range(1,8-i):
		print("",end=" ")
	for j in range(1,i+1):
		print(m,end="")
		m+=1
	m-=2
	for k in range(1,i):
		print(m,end="")
		m-=1
	print()