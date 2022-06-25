a=[]
print("Enter the no. for matrix = ")
for i in range(3):
	b=[]
	for j in range(3):
		k=int(input(" "))
		b.append(k)
	a.append(b)
print("Matrix is = ")
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
	for j in range(3):
		print(a[i][j],end=' ')
		c[j][i]=a[i][j]
	print()

print("Transpose of matrix is = ")
for i in range(3):
	for j in range(3):
		print(c[i][j],end=' ')
	print()