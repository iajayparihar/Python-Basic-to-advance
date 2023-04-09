# : Removes the item with the specified key from the dictionary and returns its value. If key is not found and default is not provided, a KeyError is raised.

my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.pop("banana")) # Output: 2
print(my_dict) # Output: {"apple": 1, "orange": 3}

