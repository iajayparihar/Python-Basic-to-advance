a=[]
print("Enter the no. for matrix = ")
for i in range(3):
	b=[]
	for j in range(3):
		k=int(input(" "))
		b.append(k)
	a.append(b)
print("Matrix is = ")

left=[]
for i in range(3):
	sum=0
	for j in range(3):
		sum+=a[i][j]
		print(a[i][j],end=' ')
	left.append(sum)
	print()


print("sum of column is =")

# for j in range(3):
# 	sum=0
# 	for i in range(3):
# 		sum+=a[j][i]
print(sum,end=' ')


