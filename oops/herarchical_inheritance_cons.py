class Student:
	def __init__(self,r,str):
		self._rollno=r
		self.__name=str
	def putName(self):
		return self.__name
class Science(Student):
	def __init__(self,x,u,p,c,m):
		Student.__init__(self,x,u)
		self.__phy=p
		self.__che=c
		self._maths=m
	def display(self):
		print("Roll No = ",self._rollno)
		print("Name = ",self.putName())
		print("physics = ",self.__phy)
		print("chemistry = ",self.__che)
		print("Maths = ",self._maths)

class Commerce(Student):
	def __init__(self,x,u,e,m,a):
		Student.__init__(self,x,u)
		self.__eco=e
		self.__mgt=m
		self._acc=a
	
	def display(self):
		print("Roll No = ",self._rollno)
		print("Name = ",self.putName())
		print("Economic = ",self.__eco)
		print("Management = ",self.__mgt)
		print("Account = ",self._acc)
#__main__
k=Science(120,"ABhigyan",55,56,57)
s=Commerce(121,"Ajayyy",98,87,86)
k.display()
s.display()





