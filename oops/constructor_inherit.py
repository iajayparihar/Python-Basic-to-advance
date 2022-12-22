class Student:
    def __init__(self,r,n):
        self.rollno=r
        self.name=n
class Sports:
    def __init__(self,sm):
        self.sportmarks=sm
class Marks(Student,Sports):
    def __init__(self, rol, nam,p,c,m,sm):
        Student.__init__(self,rol,nam)
        Sports.__init__(self, sm)
        self.phy=p
        self.che=c
        self.maths=m
    def display(self):
        print("-----------------")
        print("the Roll No. is ",self.rollno)
        print("the name is ",self.name)
        print("the sport marks is ",self.sportmarks)
        print("physics ",self.phy)
        print("chemistry ",self.che)
        print("maths ",self.maths)
        print("-----------------")

k=Marks(10,"Abhigyan",78,56,98,50)
k.display()