print("Small letter to Capital letter")
str=input("enter the string ")
l=len(str)
add=32
for i in range(l):	
	a=str[i]
	b=ord(a)
	c=b-add
	print(chr(c),end="")
	