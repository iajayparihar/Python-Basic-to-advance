class Student:
	def getData(self,r,str):
		self._rollno=r
		self.__name=str
	def putName(self):
		return self.__name
class Science(Student):
	def getMarks(self,p,c,m):
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
	def getMarks(self,e,m,a):
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
k=Science()
s=Commerce()
k.getData(120,"ABhigyan")
k.getMarks(55,56,57)
s.getData(121,"Ajayyy")
s.getMarks(98,87,86)
k.display()
s.display()





