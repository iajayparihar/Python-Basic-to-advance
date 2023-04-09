# the write() method writes a single string to a file, 
# while the writelines() method writes a sequence of strings (e.g. a list) to a file.

writefile = open('second.txt','w')
stud=''
for i in range(3):
    name = input("Enter the name :- ") +" "
    sname = input("Enter Sirname :- ") + " "
    mob = input("Enter mobile no :- ")
    data = name + sname + mob + "\n"
    writefile.write(data)
writefile.close()