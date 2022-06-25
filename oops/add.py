class Add:
	def getData(self,x,y):
		self.a=x
		self.b=y

	def putData(self):
		print("a=",self.a)
		print("b=",self.b)

	def calculate(self):
		return(self.a+self.b)
#-- main--
k=Add()
k.getData(6,54)
k.putData()
print("a+b=",k.calculate())