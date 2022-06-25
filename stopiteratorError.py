import sys
try:
	l=[2,4,6]
	i=iter(l)
	print('value=',next(i))
	print('value=',next(i))
	print('value=',next(i))
	print('value=',next(i))
except StopIteration as e:
		print("error",e)