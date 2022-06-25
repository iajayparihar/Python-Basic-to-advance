class Student:
	rollno=0
	name=""
	def getData(self,x,y):
		self.rollno=x
		self.name=y
class Marks(Student):
	phy=0
	che=0
	maths=0
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
#__main__
k=Marks()
k.display()
k.getData(124,"Ajayyy")
k.getMarks(56,45,45)
k.display()