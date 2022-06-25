import math
print("1+x-x^2+x^3-x^4.....+ x^n = ?")


n=int(input("Enter the Range = "))
x=int(input("Enter the value of x = "))
sum=1
for i in range(1,n+1):
	if(i%2==1):
		sum+=math.pow(x,i)
	else:
		sum-=math.pow(x,i)
print("Answer=",sum)