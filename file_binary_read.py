import pickle
f=open("student1.txt","rb")
print("Read data from a file")
try:
    while True:
        data=pickle.load(f)
        for record in data:
            print("Rollno =",record[0])
            print("name =",record[1])
            print("marks =",record[2])
            print("precentage =",record[3])
except Exception as e:
    print(e)
f.close()