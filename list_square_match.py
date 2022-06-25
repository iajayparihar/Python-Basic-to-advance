l=[1,2,3,4,6,9,7,49,5,25]
length=len(l)
for i in range(length):
	a=l[i]*l[i]
	for j in range(length):
		if(a==l[j]):
			print(l[i])
			break