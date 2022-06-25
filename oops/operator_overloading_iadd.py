class Complex:
	def __init__(self,x,y):
		self.real=x
		self.image=y
	def display(self):
		print("Real=",self.real)
		print("Image=",self.image)
	def __iadd__(self,m):
		self.real+=m.real
		self.image+=m.image
		return self
#__main__
p=Complex(2.3,3.2)
k=Complex(1.5,3.1)
p.display()
k.display()
p+=k
p.display()