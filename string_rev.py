str=input("enter the string=> ")
length=len(str)
print(length)
# length containe total letters => Hello = 5
for i in range(-1,-(length+1),-1):
# for i in range((length-1),-1,-1):
	print(str[i],end="")
