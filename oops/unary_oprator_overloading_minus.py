class Minus:
	def __init__(self,x,y,z):
		self.a=x
		self.b=y
		self.c=z
	def display(self):
		print("a=",self.a)
		print("a=",self.b)
		print("a=",self.c)
	def __neg__(self):
		self.a=-self.a
		self.b=-self.b
		self.c=-self.c
#__main__
k=Minus(4,-12,9)
k.display()
-k
k.display()