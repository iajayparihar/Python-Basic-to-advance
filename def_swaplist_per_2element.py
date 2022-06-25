def swaplist(xlist):
	l=[]
	a=0
	if len(xlist)%2==1:
		return print("add 1 more element in list ")
	else:
		for i in range(len(xlist)):
			l.append(a)	
	
	for j in range(len(xlist)):
		if j%2==0:
			l[j+1]=xlist[j]
			
		else:
			l[j-1]=xlist[j]
	return l
#--main--
list=[1,5,8,6,11,9,10,31]
print(swaplist(list))