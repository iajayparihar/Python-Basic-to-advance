f=open("stud1.txt","r")
data1=f.read(5)
print(data1)
print(f.tell()) #cursor position at 5
print(f.read(3))
print(f.tell()) #cursor position at 8
f.close()