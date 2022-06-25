n=int(input("enter the no.=> "))
a=n
rev=0
while(n>0):
	r=n%10
	rev=rev*10+r
	n//=10

first=rev%10
last=a%10
sum=first+last
print("first",first)
print("last",last)
print("the sum of first and last no. is=>",sum)
