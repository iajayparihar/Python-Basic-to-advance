readfile = open("print.txt","r")
data_read = readfile.read()
print(data_read)

readfile.seek(0) # for reset cursor 

data_readlines = readfile.readlines()
print(data_readlines)
readfile.close()