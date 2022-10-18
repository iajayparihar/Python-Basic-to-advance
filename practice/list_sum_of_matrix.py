def printMatrix(A):
	for i in range(3):
		for j in range(3):
			print(A[i][j],end=' ')
		print()

def inputmatrix():
	a=[]
	print("Enter the no. for  matrix = ")
	for i in range(3):
		b=[]
		for j in range(3):
			k=int(input(" "))
			b.append(k)
		a.append(b)
	return a

print("first matrix")
a=inputmatrix()
print("second matrix")
x=inputmatrix()

print("Matrix A is = ")
printMatrix(a)
print("Matrix B is = ")
printMatrix(x)

'''addition'''

print("sum of Matrix is =")

for i in range(3):
	sum=0
	for j in range(3):
		sum=a[i][j]+x[i][j]
		print(sum,end=' ')
	print()










