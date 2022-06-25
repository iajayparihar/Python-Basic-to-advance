myfile=open("E://abhipy//student.txt","w")
for i in range(5):
    name=input("Enter the name")
    myfile.write(name)
    myfile.write('\n')
myfile.close()