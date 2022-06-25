class Square:
	def getData(self,x):
		self.a=x

	def putData(self):
		print("a=",self.a)

	def calculate(self):
		return(self.a*self.a)
#-- main--
k=Square()
k.getData(int(input("enter the no.")))
k.putData()
print("Square of a is =",k.calculate())