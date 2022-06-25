str=input("ENter the string = ")
str=str.lower()
l=len(str)
for i in range(l):
	if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
		print(str[i],end=" ") 
		
'''	x=ord(str[i])
	if(97==x):
		print(chr(x),end=" ")
	elif(101==x):
		print(chr(x),end=" ")
	elif(105==x):
		print(chr(x),end=" ")
	elif(111==x):
		print(chr(x),end=" ")
	elif(117==x):
		print(chr(x),end=" ")
'''

