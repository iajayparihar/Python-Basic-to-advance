try :
	l=[3,5,7,8]
	a=int(input("Enter the no = "))
	b=int(input("Enter the no = "))
	c=a/b
	l[5]=44
	print("Answer =",c)
	print("list is =",l)

except ZeroDivisionError as e:
	print("Error:-",e)
except IndexError as e:
	print("Error=",e)
c=a+b
print("Addition =",c)