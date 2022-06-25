class Simple:
	def __init__(self,*args):
		if len(args)>1:
			self.ans=0
			for i in args:
				self.ans+=i
		elif isinstance(args[0],int):
			self.ans=args[0]*args[0]
		elif isinstance(args[0],str):
			self.ans="Hello"+args[0]
#__main__
k=Simple(1,2,3,4,5)
print("sum of list is =",k.ans)
m=Simple(4)
print("square is =",m.ans)
s=Simple("Python")
print("Message is =",s.ans)
