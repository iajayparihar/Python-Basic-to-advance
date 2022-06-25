class Student:
	def __init__(self,x,y):
		self.__rollno=x
		self._name=y
	def putRollno(self):
		return(self.__rollno)
class Marks(Student):
	def __init__(self,r,str,p,c,m):
		Student.__init__(self,r,str)
		self.__phy=p
		self.__che=c
		self.__maths=m
	def display(self):
		print("Roll No = ",self.putRollno())
		print("Name = ",self._name)
		print("physics = ",self.__phy)
		print("chemistry = ",self.__che)
		print("Maths = ",self.__maths)
#__main__
k=Marks(124,"Ajayyy",56,99,45)
k.display()