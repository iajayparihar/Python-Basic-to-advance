class Simple:
	def getData(self,x,y):
		self.a=x
		self.b=y
	def putData(self):
		print("a=",self.a)
		print("b=",self.b)
#-- main--
k=Simple()
k.getData(4,54)
k.putData()