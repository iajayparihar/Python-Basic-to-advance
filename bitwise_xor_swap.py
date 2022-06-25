print("Bitwise ^ XOR operator using swap variable")
a=int(input("enter the first no. a= "))
b=int(input("enter the second no. b="))
a=a^b
b=a^b
a=a^b
print("a=",a,"b=",b)