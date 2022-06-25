print("Take 5 subject marks ,if total markes is graterthen 400 then give +3 bouns markes or total markes is graterthen 450 then give +5 markes !")
m1=int(input("enter your DBMS markes                          "))
m2=int(input("enter your Computer network markes              "))
m3=int(input("enter your software Engineering and UML markes  "))
m4=int(input("enter your Algorithm Design markes              "))
m5=int(input("enter your  JAVA markes                         "))
total=m1+m2+m3+m4+m5
bon=0
if total>=400:
	bon=3
if total>=450:
	bon=5
print("Markes without bonus",total)
print("Markes with bonus",total+bon)