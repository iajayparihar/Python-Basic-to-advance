from multipledispatch import dispatch
@dispatch (int, int)
def product(x,y):
	return x*y
@dispatch (int ,int,int)
def product(x,y,z):
	return (x*y*z)
#__main__
print("answer=",product(5,4))
print("answer=",product(5,4,2))