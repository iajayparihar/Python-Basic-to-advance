try :
	f=open("myfile123.txt","r")
except IOError as e:
	print("Error",e)