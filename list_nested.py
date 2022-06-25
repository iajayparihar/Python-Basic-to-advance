a=[]
print("Enter the no. for matrix = ")
for i in range(3):
	b=[]
	for j in range(3):
		k=int(input(" "))
		b.append(k)
	a.append(b)
print("Matrix is = ")
for i in range(3):
	for j in range(3):
		print(a[i][j],end=' ')
	print()

