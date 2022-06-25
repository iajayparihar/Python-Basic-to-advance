import pickle
f= open ("student1.txt","rb")
print("search record from a file")
rollno =int(input("Enter the rollno ="))
found=0
try:
	while True:
		data=pickle.load(f)
		for record in data:
			if record[0]==rollno:
				print("rollno =",record[0])
				print("name =",record[1])
				print("marks =",record[2])
				print("precentage =",record[3])
				found=1
				break
except Exception:
	f.close()
if found==0:
	print("Record not Found in file")