f=open("stud1.txt","r")
print(f.tell()) # cursor position 0

f.seek(9) #shift cursor position at 9

print(f.tell())# cursor position 9
data=f.read(5)# cursor position 14
print(data)
print(f.tell()) # cursor position 14
f.close()