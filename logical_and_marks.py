print("Enter your total marks outof 500 , if total marks is graterthan 400 and you are sportperson then give 10 marks,or if total marks is graterthan 350 and you are sportperson then give 8 marks,or your tatal marks is lessthen 350 and you are sport person then give 5 marks ")
print("And if total marks is graterthan 400 and you are in NCC then give 15 marks,or if total marks is graterthan 350 and you are in NCC then give 10 marks,or your tatal marks is lessthen 350 and you are in NCC then give 8 marks ")
print()


tmarks=int(input("enter the 5 subject markes outoff 500 =>"))
sp=input("Are you sportperson y / n => ")
ncc=input("Are you in NCC  y / n =>   ")

if tmarks>=400 and sp=='y':
	smarks=10
elif tmarks>=350 and sp=='y':
	smarks=8
elif tmarks<350 and sp=='y':
	smarks=5
else:
	smarks=0

if tmarks>=400 and ncc=='y':
	nmarks=15
elif tmarks>=350 and ncc=='y':
	nmarks=10
elif tmarks<350 and ncc=='y':
	nmarks=8
else:
	nmarks=0

s=smarks+nmarks
sum=tmarks+smarks+nmarks
print("additional markes ",s)
print("know total markes is => ",sum)
p=sum/5
print("present is =>" ,p)














