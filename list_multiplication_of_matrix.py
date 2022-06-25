'''first matrix'''
a=[]
print("Enter the no. for A matrix = ")
for i in range(3):
	b=[]
	for j in range(3):
		k=int(input(" "))
		b.append(k)
	a.append(b)
print("Matrix A is = ")
for i in range(3):
	for j in range(3):
		print(a[i][j],end=' ')
	print()

'''second matrix'''

x=[]
print("Enter the no. for B matrix = ")
for y in range(3):
	v=[]
	for z in range(3):
		k=int(input(" "))
		v.append(k)
	x.append(v)
print("Matrix B is = ")
for i in range(3):
	for j in range(3):
		print(x[i][j],end=' ')
	print()

'''multiplication'''

print("multiplication of Matrix is =")
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
	for j in range(3):
		for k in range(3):
			c[i][j]+=a[i][k]*x[k][j]
		print(c[i][j],end=' ')
	print()










