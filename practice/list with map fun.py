def sq(n):
    return n>5
def addtwolist(x,y):
    if x>y:
        x=0
    return x
list_1=[23,20,5,60,4,70,8,9]
list_2=[23,2,5,6,4,7,8,9]
after_sq=list(map(addtwolist, list_1,list_2))
print(after_sq)
# after_sq=list(filter(sq, list_1))
# print(after_sq)

# after_sq=list(map(addtwolist, list_1,list_2))
# print(after_sq)

