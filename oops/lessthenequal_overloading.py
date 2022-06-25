class Compare:
	def __init__(self,x):
		self.a=x
	def __le__(self,p):
		if(self.a<=p.a):
			return True
		else:
			return False
#__ Main __
k=Compare(6)
s=Compare(6)
if k<=s:
	print("Object1 is lessthan equal obj2")
else:
	print("object1 is greater than obj2")