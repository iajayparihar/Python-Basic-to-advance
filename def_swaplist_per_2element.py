# swap with next number 
#         list [1,2,3,4]
#  swaped list [2,1,4,3]
def swaplist(xlist):
	l=[]
	a=0
	if len(xlist)%2==1: # even no. of element in list
		return print("add 1 more element in list ")
	else:
		for i in range(len(xlist)):
			l.append(a)	
	# now l is [0,0,0,0,0,0] contain all zero's
	for j in range(len(xlist)):
		if j%2==0:
			l[j+1]=xlist[j]
		else:
			l[j-1]=xlist[j] #-------means
	return l
#--main--
list=[1,5,8,6,11,9,10,31]
print(list)
print(swaplist(list))