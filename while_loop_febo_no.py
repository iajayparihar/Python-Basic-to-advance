
n=int(input("Enter the no. "))
f1=-1
f2=1
while n>0:
	f=f1+f2
	f1=f2
	f2=f
	n-=1
print("the febonaccies no.",f)