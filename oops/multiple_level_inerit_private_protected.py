class Student:
	def getData(self,r,str):
		self.__rollno=r
		self.name=str
	def putRollno(self):
		return self.__rollno
class Sports:
	def getSportMarks(self,s):
		self.__sportmarks=s
	def putSportMarks(self):
		return self.__sportmarks

class Marks(Student,Sports):
	def getMarks(self,p,c,m):
		self.__phy=p
		self.__che=c
		self._maths=m
	
	def display(self):
		print("Roll No = ",self.putRollno())
		print("Name = ",self.name)
		print("physics = ",self.__phy)
		print("chemistry = ",self.__che)
		print("Maths = ",self._maths)
		print("Sport Marks = ",self.putSportMarks())
#__main__
k=Marks()
k.getData(232,"abhigyan")
k.getMarks(45,55,59)
k.getSportMarks(69)
k.display()