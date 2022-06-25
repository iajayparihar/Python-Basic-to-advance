class Student:
	def __init__(self,r,str):
		self.__rollno=r
		self.name=str
	def putRollno(self):
		return self.__rollno
class Sports:
	def __init__(self,s):
		self.__sportmarks=s
	def putSportMarks(self):
		return self.__sportmarks

class Marks(Student,Sports):
	def __init__(self,x,a,p,c,m,sa):
		Student.__init__(self,x,a)
		Sports.__init__(self,sa)
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
k=Marks(232,"abhigyan",45,55,59,69)
k.display()



