d1={5:"deep",7:"AJAYYY",8:"sajid",4:"yatin",1:"gunnu"}
dic={}
print(d1)
sort_keys=sorted(d1.keys())
print(sort_keys)

for i in sort_keys:
	for j in sort_keys:
		if i==j:
			#dic is empty dictionary and d1 is iterarive dictionary
			dic[i]=d1[i]
			break

print(dic)