first=0
second=0
third=0
fourth=0

for i in range(5):
	third=second
	n=int(input("Enter the no.=> "))
	for j in range(2):
		second=first
		
		if(n>first):
			first=n
		
	
print(first,second,third,fourth)