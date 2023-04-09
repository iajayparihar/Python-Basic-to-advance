read1 = open("ajay.txt","r")
read2 = open("stud.txt","r")
write = open("copedFile.txt","w")

data1= read1.read()
write.write(data1+"\n")

data2 = read2.read()
write.write(data2)

read1.close()
read2.close()
write.close()

#---------
read = open("copedFile.txt","r")
print(read.read())
read.close()