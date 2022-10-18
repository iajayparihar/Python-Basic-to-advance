t=(2,4,5,6,9)
print("Tuple before modification is=",t)
# t[0]=10
l=list(t)
l[0]=12
t=tuple(l)
print("tuple after modify is = ",t)