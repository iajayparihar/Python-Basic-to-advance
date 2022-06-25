def calculate(p,r=2,t=12):
	o=p*r*t/100
	return o
#-- main --
print("Intrest is =", calculate(2000))
print("Intrest is =", calculate(1000,1.5))
print("Intrest is =", calculate(8000,1.2,24))