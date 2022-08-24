def greatest(arr,grtNo):
    for i in range(len(arr)):
        if arr[i]>grtNo:
            grtNo=arr[i]
    return grtNo

print("Enter the no we find greatest no. among them .")
k=[]
g=[]
gtemp=0
for j in range(5):
    n=int(input("Enter the no = "))
    k.append(n)

for h in range(3):
    gtemp=k[h]
    No=greatest(k,gtemp)
    g.append(No)
    k.remove(No) 
print(g)

sum=0
for i in range(len(g)):
    sum=sum+g[i]
print(sum)