class Reverse:
	def getData(self,x):
		self.n=x
	def calculate(self):
		self.k=0
		while (self.n > 0):
			j=self.n%10
			self.k=self.k*10+j
			self.n=self.n//10
		return self.k