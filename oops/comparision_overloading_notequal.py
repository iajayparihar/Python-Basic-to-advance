class Equal:
	def getData(self,x):
		self.a=x
	def __ne__(self,p):
		if(self.a==p.a):
			return True
		else:
			return False
#__ Main __
k=Equal()
s=Equal()
k.getData(12)
s.getData(10)
if k!=s:
	print("Objects are Equal")
else:
	print("object are not Same")