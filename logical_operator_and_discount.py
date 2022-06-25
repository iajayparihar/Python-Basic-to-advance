print("Find the discount if amount is graterthen 40000 and age is 60+ then give 20% dis ,30000=10% dis , lessthen 30000 is no discount")
amt=int(input("enter the amount :- "))
age=int(input("enter your age :-  "))
dis=0
if amt>=40000 and age>=60:
	dis=amt*20/100
elif amt>=30000 and age>=45:
	dis=amt*10/100
else:
	dis=0
print("net discount:-",amt-dis)	