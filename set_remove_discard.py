s1={6,7,8,5,3,2}
print(s1)
s1.discard(8)
print(s1)
s1.discard(4)
print(s1)

s1.remove(3)
print(s1)
s1.remove(1) # 1 is not present in set so remove method give error thats why we use discard method
print(s1)

'''
remove => when element is not available throw an error but discard don't.

'''