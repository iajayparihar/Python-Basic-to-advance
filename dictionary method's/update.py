# if key already present in the dictionary then update value 
# if key not present in the dict then add key and value to the dict

my_dict = {"apple": 1, "banana": 2, "orange": 3}
my_dict.update({"banana": 4, "grape": 5})
print(my_dict) # Output: {"apple": 1, "banana": 4, "orange": 3, "grape": 5}