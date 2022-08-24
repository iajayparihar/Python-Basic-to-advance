class Square:
	def __init__(self):
		self.n=2
	def getNo(self,x):
		self.n=x
	def calculation(self):
		return(self.n*self.n)
		
#__ main__
k=Square()
print("Square is ",k.calculation())
k.getNo(5)
print("Square is ",k.calculation())