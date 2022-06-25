L=[{'1':"rohit",'2':"ajay",'3':"yatin",'4':"deep",'5':"rohit",'6':"yatin"}]

u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)



'''
print(dic)
dic1=dic.copy()
print(dic[1])
for x,y in dic.items():
	for i in range(1,len(dic)):
		if y==dic[i]:
			dic1[i]=y
		break
print(dic1)
'''