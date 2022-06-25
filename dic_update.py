key=('ten','twenty','thirty')
value=(10,20,30)
x.dict()
for i in x.keys():
	x.update(keys[i],values[i])
print(x)