d1={"a":100,"b":200,"c":300,"e":100}
d2={"a":30,"b":500,"c":50,"f":60}
print(d1)
print(d2)
dic={}
for x,y in d1.items():
	if x in d2:
		dic[x]=d2[x]+d1[x]
	else:
		dic[x]=d1[x]
for a,b in d2.items():
	if a in d1:
		dic[a]=d1[a]+d2[a]
	else:
		dic[a]=d2[a]
print(dic)