class Compare:
	def __init__(self,x):
		self.a=x
	def __lt__(self,p):
		if(self.a<p.a):
			return True
		else:
			return False
#__ Main __
k=Compare(8)
s=Compare(6)
if k<s:
	print("Object1 is lessthan obj2")
else:
	print("object1 is greater than obj2")