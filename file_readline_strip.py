filein=open("marks.txt","r")
while str:
    str=filein.readline()
    print(str,":=",len(str))
    str1=str.rstrip()
    print(str1,":=",len(str1))
filein.close()