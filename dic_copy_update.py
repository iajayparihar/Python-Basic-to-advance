dic1={'ten':10,'twenty':20}
dic2={'thirty':30,'fourty':40,'twenty':20}
x=dic1.copy()
print(dic1)
print(dic2)
print(x)
x.update(dic2) #discard duplicate
print(x)