tmarks=int(input("enter the 5 subject markes outoff 500 =>"))
sp=input("Are you sportperson y / n => ")
ncc=input("Are you in NCC  y / n =>   ")
if ncc=='y' and sp=='y':
	emarks=20
elif ncc=='y' and sp=='n':
	emarks=10
elif ncc=='n' and sp=='y':
	emarks=5
else:
	emarks=0
sum=tmarks+emarks
print("total markes=>",sum)
p=sum/5
print("present=>",p)	