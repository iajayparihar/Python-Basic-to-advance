a=[]
print("Enter the no. for matrix = ")
for i in range(3):
	b=[]
	for j in range(3):
		k=int(input(" "))
		b.append(k)
	a.append(b)
fdig=0
print("Matrix is = ")
for i in range(3):
	for j in range(3):
		print(a[i][j],end=' ')
		if(i==j):
			fdig+=a[i][j]
	print()
print("the sum of First digonal is =",fdig)
sdig=0
for i in range(3):
	for j in range(2,-1,-1):
		if(j+i==2):
			sdig+=a[i][j]
			break
print("the sum of Second digonal is =",sdig)












