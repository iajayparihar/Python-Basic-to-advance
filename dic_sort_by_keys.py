d1={5:"deep",7:"AJAYYY",8:"sajid",4:"yatin",1:"gunnu"}
dic={}
print(d1)
sort_keys=sorted(d1.keys())

for i in sort_keys:
	for j in sort_keys:
		if i==j:
			dic[i]=d1[i]
			break

print(dic)