class Plus:
	def __init__(self,x):
		self.a=x
	def __add__(self,m):
		return(self.a+m.a)
#__main__
k=Plus(int(input("Enter the no=")))
s=Plus(int(input("Enter the no=")))
print("Adition =",k+s)
t=Plus(input("Enter the String="))
p=Plus(input("Enter the String="))
print("Concatenation=",t+p)