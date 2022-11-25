# file=open("pythonFile1.txt","w")
# file.write("this is my first practic program .")
# file.close()

# file=open("pythonFile1.txt","r")
# text=file.read()
# newfile=open("ajay.txt","w")
# newfile.write(text)
# # newfile.close()
# print(text)
address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
with open("ajay.txt","a") as f:
    f.write("Venom")
    f.writelines(address)

