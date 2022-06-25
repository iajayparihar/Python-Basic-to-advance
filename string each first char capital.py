n=input("enter ")
l=len(n)

for i in range(-1,l):
	ch=n[i]

	if(i==0 or ch==' '):
		ch= n[i+1]
		ns=ord(ch)
		
		if ns>=97 and ns<=122:
			ns-=32
			ns=chr(ns)
			i+=1
			n=n[:i]+ns+n[i+1:]
print("New String",n)


