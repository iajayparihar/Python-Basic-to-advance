import pickle
import os
f=open("student1.txt","rb")
f1=open("temp5.txt","wb")
print("Update record from a file")
rollno=int(input("Enter the rollno ="))
found=0
try:
    while True:
        data=pickle.load(f)
        for record in data:
            if record[0]==rollno:
                record[1]=input("Enter the new name = ")
                record[2]=int(input("enter the marks = "))
                record[3]=record[2]/5
                found=1
                break
        pickle.dump(data, f1)
except Exception:
    f.close()
    f1.close()
os.remove("student1.txt")
os.rename("temp5.txt", "student1.txt")
if found==0:
    print("Record not found in file")
else:
    print("record updated successfully")