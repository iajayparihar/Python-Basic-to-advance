class stud:
    def __init__(self,name):
        self.name = name 
        
    def __str__(self):
        # return repr(['hello','Abhigyan'])
        return '--->  default __str__ run when we print the class object ' + self.name

    # def show(self):


k = stud('venom')
print(k)