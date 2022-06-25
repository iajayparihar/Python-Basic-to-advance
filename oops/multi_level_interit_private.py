class Student:
	def getData(self,x,str):
		self.__rollno=x
		self.__name=str
	def putRollno(self):
		return self.__rollno
	def putName(self):
		return self.__name

class Marks(Student):
	def getMarks(self,p,c,m):
		self.__phy=p
		self.__che=c
		self._maths=m
	def putPhy(self):
		return self.__phy
	def putChe(self):
		return self.__che	
class Calculation(Marks):
	def calculate(self):
		self.total=self.putPhy()+self.putChe()+self._maths
	def display(self):
		print("Roll No = ",self.putRollno())
		print("Name = ",self.putName())
		print("physics = ",self.putPhy())
		print("chemistry = ",self.putChe())
		print("Maths = ",self._maths)
		print("Total = ",self.total)
#__main__
k=Calculation()
k.getData(232,"abhi")
k.getMarks(45,55,59)
k.calculate()
k.display()