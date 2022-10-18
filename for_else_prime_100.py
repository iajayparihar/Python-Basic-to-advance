# 1 is not a prime NO. 
# prime no, start from 2
for j in range (2, 101):	
	for i in range(2,j):
		if(j % i == 0):
			break
	else:
		print(j,end=" ")
