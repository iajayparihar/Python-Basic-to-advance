import math 
print("1+x-x^2/2!+x^3/3!-x^4/4!......x^n/n!")

n=int(input("Enter the Range = "))
x=int(input("Enter the value of x = "))
sum=1
f=1
for i in range(1,n+1):
	f=f*i
	if(i%2==1):
		sum+=math.pow(x,i)/f
	if(i%2==0):
		sum-=math.pow(x,i)/f
print("Answer=>",sum)