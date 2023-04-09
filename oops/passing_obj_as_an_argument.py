class Copyobj:
	def getData(self,x,y):
		self.a=x
		self.b=y
	def display(self):
		print("a=",self.a)
		print("b=",self.b)
	def copy(self,m):
		self.a=m.a
		self.b=m.b
		m.a+=5
		m.b+=7
		
#__main__
p=Copyobj()
k=Copyobj()
p.getData(5,7)
k.copy(p)
p.display()
k.display()
print("k obj ",k.__dict__)
print("p obj ",p.__dict__)