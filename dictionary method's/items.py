# items() method is used to make dict iterable
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.items()) # Output: dict_items([('apple', 1), ('banana', 2), ('orange', 3)])

for key,value in my_dict.items():
    print(key," ",value)

# normal dictionary is not iterable in key value 
# for key,value in my_dict:
#     print(key," ",value)