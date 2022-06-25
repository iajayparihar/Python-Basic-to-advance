import pickle
f=open("student1.txt","rb")
f1=open("stud2.txt","wb")
print("copy record file")
found=0
try:
    while True:
        data=pickle.load(f)
        for record in data:
            found=1
            pickle.dump(data,f1)
except Exception as e:
    print(e)
f.close()
f1.close()
if found==0:
    print("record not copy in file")
else:
    print("record copped")





