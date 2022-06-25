f=open("e:\\abhipy\\myfile.txt","r")
print("name","phone no")
for line in f :
    words=line.split()
    print(words[0],"  ",words[1])
f.close()