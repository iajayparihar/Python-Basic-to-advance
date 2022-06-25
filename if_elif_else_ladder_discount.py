print("if given amount is gratherthan 40,000 then give 20% discount ... 20000=15% discount, 10000=10% discount, lessthen 10000 no discount")
print()
amt=int(input("enter your the amount "))
dis=0
if amt>=40000:
	dis=amt*.2
elif amt>=20000:
	dis=amt*.15
elif amt>=10000:
	dis=amt*.1
else:
	dis=0
print("net amount =",amt-dis)