try:
	for i in range(1,100):
		f=2.0**i
		f=f**i
		print(f)
except OverflowError as e:
	print("error",e)
else:
	print("error",e)