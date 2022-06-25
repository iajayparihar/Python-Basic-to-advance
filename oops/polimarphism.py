class Add:
	def getData(self,a,b):
		self.x=a
		self.y=b
	def calculate(self):
		return (self.x+self.y)
class Multiply:
		def getData(self,a,b):
			self.x=a
			self.y=b
		def calculate(self):
			return (self.x*self.y)
#__main__
p=Add()
k=Multiply()
for i in (p,k):
	i.getData(int(input("Enter the First no=")),int(input("Enter the Second no=")))
	print("Answer=",i.calculate())