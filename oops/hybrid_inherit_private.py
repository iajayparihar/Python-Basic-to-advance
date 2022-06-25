class Student:
	def getData(self,r,str):
		self.__rollno=r
		self.name=str
	def putRollno(self):
		return self.__rollno
class Sports(Student):
	def getSportMarks(self,s):
		self._sportmarks=s

class Marks(Student):
	def getMarks(self,p,c,m):
		self.__phy=p
		self._che=c
		self.maths=m
	def putPhy(self):
		return self.__phy
class Calculation(Marks,Sports):
	def Calculate(self):
		self.__total=self.putPhy()+self._che+self.maths+self._sportmarks	
	def display(self):
		print("Roll No = ",self.putRollno())
		print("Name = ",self.name)
		print("physics = ",self.putPhy())
		print("chemistry = ",self._che)
		print("Maths = ",self.maths)
		print("Sport Marks = ",self._sportmarks)
		print("total = ",self.__total)
#__main__
k=Calculation()
k.getData(232,"abhi")
k.getMarks(45,55,59)
k.getSportMarks(70)
k.Calculate()
k.display()