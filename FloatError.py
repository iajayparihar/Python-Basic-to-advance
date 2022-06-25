import math 
try:
	k=math.exp(1100)
	print("Answer",k)
except FloatingPointError as e:
	print("error",e)