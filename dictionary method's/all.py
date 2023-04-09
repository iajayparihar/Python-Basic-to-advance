# create a dictionary
my_dict = {"apple": 1, "banana": 2, "orange": 3}

# clear() method
my_dict.clear()
print(my_dict) # Output: {}

# copy() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
copy_dict = my_dict.copy()
print(copy_dict) # Output: {"apple": 1, "banana": 2, "orange": 3}

# fromkeys() method
my_dict = dict.fromkeys(["apple", "banana", "orange"], 0)
print(my_dict) # Output: {"apple": 0, "banana": 0, "orange": 0}

# get() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.get("apple", 0)) # Output: 1
print(my_dict.get("grape", 0)) # Output: 0

# items() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.items()) # Output: dict_items([('apple', 1), ('banana', 2), ('orange', 3)])

# keys() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.keys()) # Output: dict_keys(['apple', 'banana', 'orange'])

# pop() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.pop("banana")) # Output: 2
print(my_dict) # Output: {"apple": 1, "orange": 3}

# popitem() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.popitem()) # Output: ('orange', 3)
print(my_dict) # Output: {"apple": 1, "banana": 2}

# setdefault() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.setdefault("apple", 0)) # Output: 1
print(my_dict.setdefault("grape", 0)) # Output: 0
print(my_dict) # Output: {"apple": 1, "banana": 2, "orange": 3, "grape": 0}

# update() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
my_dict.update({"banana": 4, "grape": 5})
print(my_dict) # Output: {"apple": 1, "banana": 4, "orange": 3, "grape": 5}

# values() method
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.values()) # Output: dict_values([1, 2, 3])
