n=int(input("enter the no:-"))
r,k=0,0
y,s=n,n

while(y>0):
	y=y//10
	r+=1
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


	