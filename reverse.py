class Reverse:
	r=0
	f=0
	def getData(self,x):
		self.a=x
		print("a=",self.a)

	def Reverse(self):
		while(self.a>0):
			self.r=self.a%10
			self.f=self.f*10+self.r
			self.a//=10
		
		return self.f

#-- main--
k=Reverse()
k.getData(int(input("enter the no.")))
print("reverse of number =",k.Reverse())