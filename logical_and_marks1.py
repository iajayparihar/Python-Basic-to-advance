print("if ncc and sp both true then give 20 or one of them is true then give 10 markes ")
tmarks=int(input("enter the 5 subject markes outoff 500 =>"))
sp=input("Are you sportperson y / n => ")
ncc=input("Are you in NCC  y / n =>   ")
if ncc=='y' and sp=='y':
	emarks=20
elif ncc=='y' or sp=='y':
	emarks=10
else:
	emarks=0
sum=tmarks+emarks
print("total markes=>",sum)
p=sum/5
print("present=>",p)	