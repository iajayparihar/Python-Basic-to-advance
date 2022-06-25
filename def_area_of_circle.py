def calculate(r,pi=3.14):
	area=pi*r*r
	return area
#-- main --
n= float(input("Enter the radius ="))
print("area of circle ", calculate(n))