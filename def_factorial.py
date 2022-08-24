def fact(x):
	if x==1:
		return 1
	elif x==0:
		return 1
	else:
		return (x*fact(x-1))
#-- main--
n=int(input("ENTER the no.="))
print("facorial is =",fact(n))