myfile=open(r'E:\abhipy\student1.txt','w')
list1=[]
for i in range(5):
    name=input("Enter the name =")
    list1.append(name+"\n")
print(list1)
myfile.writelines(list1)
myfile.close()