myfile=open("myfile.txt")
str1=" "
size=0
tsize=0
while str1:
    str1=myfile.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("size of file after removing all EOL char and blanks lines ",size)
print("the total size of file =",tsize)
myfile.close()