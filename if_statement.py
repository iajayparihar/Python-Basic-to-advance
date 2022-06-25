print("if your amount is graterthen 20000 then you get 20% discount! ")
amt=int(input("Enter your amount  "))
dis=0
if amt>=20000:
	dis=amt*20/100
print("net Amount is =>",amt-dis)