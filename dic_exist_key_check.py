dic={1:"rohit",2:"ajay",3:"yatin",4:"deep",5:"rohit",6:"yatin"}
print(dic)
n=int(input("enter the key :- "))
for x in dic.keys():
	if x==n:
		print("The keys is exist")
		break
else:
	print("This key is not exist")