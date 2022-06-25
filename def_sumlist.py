def sumlist(mylist):
	sum=0
	for i in mylist:
		sum+=i
	avg=sum/len(mylist)
	print("sum of list is =",sum)
	print("avg of list is =",avg)
#--main--
list=[12,0,7,8,9,]
sumlist(list)