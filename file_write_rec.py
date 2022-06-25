count=int(input("how many students are there in the class ="))
fout=open("marks.txt","w")
for i in range(count):
    print("Enter details for student ",i+1,"blow")
    rollno=int(input("Rollno = "))
    name=input("name =")
    marks=int(input("marks ="))
    rec=str(rollno)+","+name+","+str(marks)+"\n"
    fout.write(rec)
fout.close()
