for i in range(6):
	for j in range(1,7-i ):
		print('',end=" ")
	for k in range(1,i+1):
		print(k,end="")
	for q in range(i-1,0,-1):
		print(q,end="")
	print()