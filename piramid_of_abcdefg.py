for i in range(7,0,-1):
	m=65
	for j in range(1,i+1):
			print(chr(m),end="")
			m+=1
	if i==7:
		m-=2
		s=i-1
		t=0
	else:
		m-=1
		s=i
		t=t+1
	for k in range(1,(7-i)+t):
		print("",end=" ")
	for l in range(1,s+1):
		print(chr(m),end="")
		m=m-1
	print()