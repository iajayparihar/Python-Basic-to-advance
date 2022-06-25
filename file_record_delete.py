import pickle
import os
f=open("student1.txt","rb")
f1=open("temp32.txt","wb")
print("delete record from a file")
rollno=int(input("Enter the rollno ="))
found=0
try:

	while True:
		data=pickle.load(f)
		for record in data:
			if record[0]==rollno:
				found=1
				continue
			pickle.dump(data,f1)
except Exception:
	f.close()
	f1.close()
os.remove("student1.txt")
os.rename("temp32.txt","student1.txt")
if found==0:
	print('record not found in file')
else:
	print('record deleted successfully')




