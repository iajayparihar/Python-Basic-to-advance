a=10
def add(x,y):
    global a
    a=5
    print("function :- ",a)
    c=x+y+a
    return c
print(a)
x= add(5, 2)
print(x)