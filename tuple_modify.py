t=(2,4,5,6,9)
print("Tuple before modification is=",t)

l=list(t)
l[2]=12
t=tuple(l)
print("tuple after modify is = ",t)