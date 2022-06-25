w=input("enter the txt=")
l=len(w)
for i in range(l+1):
	for j in range(i):
		print(w[j],end="")
	print()