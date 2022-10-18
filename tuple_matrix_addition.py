def printMatrix(t):
	for i in range(len(t)):
		for j in range(len(t)):
			print(t[i][j],end=" ")
		print()
tup1=((2,4,6),(6,9,12),(8,7,10))
tup2=((2,3,5),(1,5,7),(8,7,3))
# print("first matrix is =")
# for i in range(len(t)):
# 	for j in range(len(t)):
# 		print(t[i][j],end=" ")
# 	print()
# print("Second matrix is =")
# for i in range(len(t1)):
# 	for j in range(len(t1)):
# 		print(t1[i][j],end=" ")
# 	print()

print("first matrix is =")
printMatrix(tup1)
print("Second matrix is =")
printMatrix(tup2)

print("Addition of matrix is =")
for i in range(len(tup1)):
	for j in range(len(tup1)):
		print(tup1[i][j]+tup2[i][j],end=" ")
	print()