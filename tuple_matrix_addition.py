t=((2,4,6),(6,9,12),(8,7,10))
t1=((2,3,5),(1,5,7),(8,7,3))
print("first matrix is =")
for i in range(len(t)):
	for j in range(len(t)):
		print(t[i][j],end=" ")
	print()
print("Second matrix is =")
for i in range(len(t1)):
	for j in range(len(t1)):
		print(t1[i][j],end=" ")
	print()
print("Addition of matrix is =")
for i in range(len(t)):
	for j in range(len(t)):
		print(t[i][j]+t1[i][j],end=" ")
	print()