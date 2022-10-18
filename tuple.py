t=(1,2,4,5,9,6)
print("interger tuple ",t)

t=()
print("Empty Tuple",t)

t=("a","b","d","f","h","e")
print("Character Tuple",t)

t=(2.3,4.5,1.6,3.33)
print("float Tuple",t)

t=(3,4.5,"a","apple")
print("Mix Tuple",t)

print("Length of Tuple",len(t))
print()

print("Traversing of Tuple")

for i in range(len(t)):
	print(t[i],end=' ')
print()
for i in t:
	print(i,end=" ")
print()










