try:
	print("press control key")
	ignore=input()
except KeyboardInterrupt:
	print('control key pressed Error')
else:
	print('No Error')