class Student:
	def getData(self,r,str):
		self.rollno=r
		self.name=str
class Sports(Student):
	def getSportMarks(self,s):
		self.sportmarks=s

class Marks(Student):
	def getMarks(self,p,c,m):
		self.phy=p
		self.che=c
		self.maths=m
class Calculation(Marks,Sports):
	def Calculate(self):
		self.total=self.phy+self.che+self.maths+self.sportmarks	
	def display(self):
		print("Roll No = ",self.rollno)
		print("Name = ",self.name)
		print("physics = ",self.phy)
		print("chemistry = ",self.che)
		print("Maths = ",self.maths)
		print("Sport Marks = ",self.sportmarks)
		print("total = ",self.total)
#__main__
k=Calculation()
k.getData(232,"abhi")
k.getMarks(45,55,59)
k.getSportMarks(70)
k.Calculate()
k.display()