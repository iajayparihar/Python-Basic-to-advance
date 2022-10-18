d={1:"jay", 3:"sona", 6:"yatin",4:"deep",2: "Abhigyan" }
print(d)
dic={}
sort_value=sorted(d.values())
# sort_value=sorted(d.keys())
for i in sort_value:
	for j in d.keys():
		if d[j]==i:
			dic[j]=d[j]
			break
		
print("sorted by value =",dic)