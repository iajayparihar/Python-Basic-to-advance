file = open("myfirstfile.txt", "r")
data = file.read()
file.close()

file1 = open("copy.txt", "w")
file1.write(data)
file1.close()

# f=open("copy.txt","r")
# print(f.read())
# f.close()

with open("a.txt", "a") as f:
    f.write(data)
