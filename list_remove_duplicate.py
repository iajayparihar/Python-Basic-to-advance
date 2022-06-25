l=[1,2,3,4,2,5,2,3]
a=[]
print('list is =',l)
for i in l:	
	if i not in a:
		a.append(i)
print('after remove duplicate element from list=',a)  
