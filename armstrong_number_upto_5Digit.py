a=input("enter the no:-")
print(list(a))
n=int(a)
k=0
y,s=n,n

r=len(a)

if (r==3):
	while(n>0):
		j=n%10
		k=k+j*j*j
		n=n//10
elif(r==4):
	while(n>0):
		j=n%10
		k=k+j*j*j*j
		n=n//10
elif(r==5):
	while(n>0):
		j=n%10
		k=k+j*j*j*j*j
		n=n//10

if(k==s):
	print("no is armstrong")
else:
	print("no is not armstrong")


	