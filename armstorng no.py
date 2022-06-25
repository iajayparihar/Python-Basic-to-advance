n=int(input("enter the no:-"))
k=0
s=n
while(n>0):
	j=n%10
	k=k+j*j*j
	n=n//10
if(k==s):
	print("no is armstrong")
else:
	print("no is not armstrong")
	
