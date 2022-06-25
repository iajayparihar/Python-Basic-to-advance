import math 
print("1+x+x^2/2,x^3/3,......+x^n/n =?")

n=int(input("Enter the Range = "))
x=int(input("Enter the value of x = "))
sum=1
for i in range(1,n+1):
	sum+=math.pow(x,i)/i	
print("Answer=",sum)

'''
p=math.pow(x,i)
	sum+=p/i

'''