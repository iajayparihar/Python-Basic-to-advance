for j in range (1, 101):
	
	for i in range(2,j):
        	if(j % i == 0):
            		break

	else:
        	print(j)
