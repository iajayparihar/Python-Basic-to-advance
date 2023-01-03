file=open("a.txt","r")
data=file.read()
# print(data)

count=0
# print(len(data))
for i in file:
    print(i)
    print("---")
    
file.close()