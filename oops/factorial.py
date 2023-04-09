class fact:
	f=1
	def getData(self,x):
		# self.f = 1
		self.a = x
		print("a=",self.a)

	def calculate(self):
		for i in range(self.a,0,-1):
			self.f=self.f*i
		return self.f

#-- main--
k=fact()
k.getData(int(input("enter the no.")))
print("Factorial =",k.calculate())
print(k.__dict__)