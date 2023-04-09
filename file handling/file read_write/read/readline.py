#-----> without readline method read the file 
read = open('first.txt','r')
for r in read:
    print(r)
read.close()

#-------> with readline method read first line then loop

read = open('first.txt','r')
line = read.readline()
while line :
    print(line)
    line = read.readline()
read.close()

#--> without read any line direct loop

read = open('first.txt','r')
line = ' '
while line :
    line = read.readline()
    print(line)
read.close()






