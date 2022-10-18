wrd=input("Enter the string ")
l=len(wrd)
nwrd=''
for i in range(l):
	if(ord(wrd[i])>=65 and ord(wrd[i])<=90):
		nwrd+=chr(ord(wrd[i])+32)
	else:
		nwrd+=wrd[i]
print("Entered word is =>",wrd)
print("lower case=>",nwrd)