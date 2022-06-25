try:
	a=[1,2,3]
	dic={"rollno":234,"name":"Ajayyy"}
	print(a[1])
	print(dic['class'])

#except IndexError as e:
	#print("error",e)
#except KeyError as e:
	#print("error",e)

except LookupError as e:
	print("error",e)
