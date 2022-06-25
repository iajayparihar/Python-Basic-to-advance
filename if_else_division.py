m1=int(input("Enter the markes of math    "))
m2=int(input("Enter the markes of physics "))
m3=int(input("Enter the markes of English "))
sum=m1+m2+m3
print("sum=",sum)
pre=sum/3
print("presentage=",pre)
if pre>60:
	print("pass in 1st division")
else:
	print("pass in 2nd division")