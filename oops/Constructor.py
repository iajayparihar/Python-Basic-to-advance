class Add:
	def __init__(self,x,y):
		self.a=x
		self.b=y
	def addition(self):
		return(self.a+self.b)
#__ main__
k=Add(5,6)
print("Addition",k.addition())
m=Add(1.3,5.6)
print("Addition",m.addition())