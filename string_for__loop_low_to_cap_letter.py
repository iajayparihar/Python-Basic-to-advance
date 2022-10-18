wrd=input("Enter the string ")
l=len(wrd)
nwrd=''
for i in range(l):
	if(ord(wrd[i])>=97 and ord(wrd[i])<=122):
		nwrd+=chr(ord(wrd[i])-32)
	else:
		nwrd+=wrd[i]
print("Entered word is =>",wrd)
print("upper case=>",nwrd)