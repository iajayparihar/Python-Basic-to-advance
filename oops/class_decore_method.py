class eval_equation:
	def __init__(self,a):
		self.ans=a
		print(self.ans)
	@classmethod
	def eq1(cls,args):
		x=cls((args[0]*args[0])+(args[1]*args[1])-args[2])
		return x
	@classmethod
	def eq2(cls,args):
		y=cls((args[0]*args[0])+(args[1]*args[1]))
		return y
	@classmethod
	def eq3(cls,args):
		temp=0
		for i in range(0,len(args)):
			temp+=args[i]*args[i]
		temp=temp/len(args)
		z=cls(temp)
		return z
	# @staticmethod(f)
	
#__main__
li=[[1,2],[1,2,3],[1,2,3,4,5]]
i=0
while i<3:
	inp=li[i]
	if len(inp)==2:
		p=eval_equation.eq2(inp)
		print("equation 2=",p.ans)
	# elif len(inp)==3:
	# 	q=eval_equation.eq1(inp)
	# 	print("equation 1=",q.ans)
	# else:
	# 	r=eval_equation.eq3(inp)
	# 	print("equation 3=",r.ans)
	i+=1
		