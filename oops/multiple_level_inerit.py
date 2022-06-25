class Student:
	def getData(self,r,str):
		self.rollno=r
		self.name=str
class Sports:
	def getSportMarks(self,s):
		self.sportmarks=s

class Marks(Student,Sports):
	def getMarks(self,p,c,m):
		self.phy=p
		self.che=c
		self.maths=m
	
	def display(self):
		print("Roll No = ",self.rollno)
		print("Name = ",self.name)
		print("physics = ",self.phy)
		print("chemistry = ",self.che)
		print("Maths = ",self.maths)
		print("Sport Marks = ",self.sportmarks)
#__main__
k=Marks()
k.getData(232,"abhi")
k.getMarks(45,55,59)
k.getSportMarks(70)
k.display()