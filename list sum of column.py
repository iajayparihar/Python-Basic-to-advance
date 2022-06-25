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


print("sum of column is =")

for j in range(3):
	sum=0
	for i in range(3):
		sum+=a[i][j]
	print(sum,end=' ')




