# if key not found in the dictionary then append the key with default value and return value
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.setdefault("apple", 69)) # Output: 1
print(my_dict.setdefault("grape", 69)) # Output: 69
print(my_dict) # Output: {"apple": 1, "banana": 2, "orange": 3, "grape": 69 }
#--------------------

# if key already present in the dictionary then update value 
# if key not present in the dict then add key and value to the dict
my_dict = {"apple": 1, "banana": 2, "orange": 3}
my_dict.update({"banana": 4, "grape": 51})
print(my_dict) # Output: {"apple": 1, "banana": 4, "orange": 3, "grape": 5}
#--------------------

#if key not present in the dictionary return the default value 
# there is not insersion in the dictionary
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict.get("apple", 0)) # Output: 1
#                  key , default value

print(my_dict.get("grape",5)) # Output: 5
print(my_dict.get("grape")) # Output: None
