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

'''addition'''

print("sum of Matrix is =")

for i in range(3):
	sum=0
	for j in range(3):
		sum=a[i][j]+x[i][j]
		print(sum,end=' ')
	print()










