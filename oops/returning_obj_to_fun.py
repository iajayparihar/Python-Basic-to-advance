class Complex:
	def __init__(self,x,y):
		self.real=x
		self.image=y
	def display(self):
		print("REAL=",self.real)
		print("image=",self.image)
	def Calculate (self,m):
		k=Complex(0,0)
		k.real=self.real+m.image
		k.image=self.image+m.image
		return k
#__main__
p=Complex(2.3,4.5)
q=Complex(3.6,2.4)
s=Complex(0,0)
s=p.Calculate(q)
p.display()
q.display()
s.display()