print("Find greatest among 3 no.using logical operator !")
a=int(input("enter the no. a= "))
b=int(input("enter the no. b= "))
c=int(input("enter the no. c= "))
if a>b and a>c:
	print("greatest A=",a)
elif b>c:
	print("greatest B=",b)
else:
	print("greateat C=",c)