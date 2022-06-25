try :
	a=int(input("Enter the no = "))
	b=int(input("Enter the no = "))
	c=a/b
	print("Answer =",c)
except ZeroDivisionError as e:
	print("Error:-",e)
c=a+b
print("Addition =",c)