print("discount calculate if age is graterthen 50 then give 5% discount or age is graterthen 60 then give 10% discount !")
amt=int(input("enter Amount    "))
age=int(input("enter your age  "))
dis=0
if age>=50:
	dis=amt*5/100
if age>=60:
	dis=amt*10/100
print("Net amount => ",amt-dis)