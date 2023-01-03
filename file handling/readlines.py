f=open("stud.txt","r") # read and readline maintain the cursor pointer
data1=f.readline()     # cursor at the first line end
print(data1)
data=f.read()          #cursor read, left unread lines
print(data)
f.close()
