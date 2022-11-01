def display(*var):
	for k in var:
		print(k)
	print(*var)
	print(type(var))
#-- main --
display("c","c++","java")

#when we call a funtion so the argument are pass as tuple 