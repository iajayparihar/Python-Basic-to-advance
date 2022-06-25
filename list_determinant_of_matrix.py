a=[]
print("Enter the no. for matrix = ")
for i in range(3):
	b=[]
	for j in range(3):
		k=int(input(""))
		b.append(k)
	a.append(b)
print("Matrix is = ")
for i in range(3):
	for j in range(3):
		print(a[i][j],end=' ')
	print()
deter=0
deter=(a[0][0]*(a[1][1]*a[2][2]-a[2][1]*a[1][2])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

print("determinant of A = ", deter)