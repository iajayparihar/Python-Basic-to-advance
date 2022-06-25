class Student:
	def getData(self,x,y):
		self.__rollno=x
		self._name=y
	def putRollno(self):
		return(self.__rollno)

class Marks(Student):
	def getMarks(self,p,c,m):
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
k=Marks()
k.getData(124,"Ajayyy")
k.name="Abhigyan"
k.getMarks(56,99,45)
k.display()