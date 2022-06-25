from multipledispatch import dispatch
class Calculation:
	@dispatch (float)
	def calculate(r):
		return 3.14*r*r
	@dispatch (float,float)
	def calculate(l,b):
		return (l*b)
	@dispatch (float,float,float)
	def calculate(half,h,b):
		return (half*h*b)
#__main__
p=Calculation()
k=Calculation()
s=Calculation()
print("Area of circle=",p.calculate(4.5))
print("Area of rectangle=",k.calculate(4.5,2.2))
print("Area of triangle=",s.calculate(4.5,2.3,1.2))
