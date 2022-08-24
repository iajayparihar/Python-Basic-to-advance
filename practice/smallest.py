def smallestno(arr,sml):
    for j in range(len(arr)):
        if arr[j]<sml:
            sml=arr[j]
    return sml

# putting element n list
print("finding among 5 no which is lowest")
k=[]
smallestNoArray=[]

for i in range(5):
    a=int(input("Enter the no. ="))
    k.append(a)
print(k)
# put 1st element in small for compare

for l in range(3):
    small=k[0]
    no=smallestno(k,small)
    smallestNoArray.append(no)
    k.remove(no)

print("smallest 3 no is =",smallestNoArray)
        