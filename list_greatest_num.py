l=[1,21,42,13,-56]
length=len(l)
a=0
for i in range(length):
	if(l[i]>a):
		a=l[i]
print("greatest no.=",a)
print("--------------------------")
a=0
for i in l:
	if(i>a):
		a=i
print("greatest no.=",a)
