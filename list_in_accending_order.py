n=["ram","ravan","Abhigyan","v"]
for i in range(len(n)):
	for j in range(i+1,len(n)):
		if(n[i]>n[j]):
			n[i],n[j]=n[j],n[i]	
print(n)