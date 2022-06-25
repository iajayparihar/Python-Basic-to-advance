n=int(input("enter the string "))
a=n
b=0
rev=0
r=0
while(n>0):
	r=n%10
	b+=r*r*r
	n//=10
if(a==b):
	print(a,"is Armstrong number")
else:
	print("Given no. is not armstrong ")