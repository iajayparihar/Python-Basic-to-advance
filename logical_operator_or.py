amt=int(input("Enter the amount "))
age=int(input("Enter age "))
dis=0
if amt>=40000 or age>=60:
	dis=amt*20/100
elif amt>=30000 or age>=45:
	dis=amt*15/100
elif amt>=20000 or age>=20:
	dis=amt*10/100
else:
	dis=0
print("discount=",dis)
print("net amount =",amt-dis)