import pickle
f=open("student1.txt","ab") 
# a= append 
# b= binary
print("Append Data")
ch='y'
while ch=='y':
    data=[]
    rollno=int(input("Enter the the rollno = "))
    sname=input("Enter student name =")
    marks=int(input("Enter the marks ="))
    per=marks/5
    data.append([rollno,sname,marks,per])
    pickle.dump(data,f)
    ch=input("Enter more record y/n =")
f.close()