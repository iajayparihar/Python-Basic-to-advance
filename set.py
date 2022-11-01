s1={1,3,2,6,4}
print(s1)
s2={1,3,2,(4,5),6,4}
print(s2)

# tuple can contain duplicate 
# set not allowed duplicate
# so in a set , tuple can contain duplicate but set not allow

s2={1,3,2,(4,5,5),6,6,4}
print(s2)
s2.add(93)
s2.remove(1)
print(s2)
# s2={(3,20,30,20)}
# print(type(s2))
# s2={1,{3,2},(4,5,5),6,6,4}
# print(s2)

'''
set is unorderd 
duplicate not allowed
only tuple is allowed for nested set's
'''
# s2={1,3,2,[4,5],6,4}
# print(s2)
# s2={1,3,2,{4,5},6,4}
# print(s2)