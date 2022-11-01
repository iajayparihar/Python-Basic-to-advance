def my_function(*kids): # tuple is passing 
    print(kids)

my_function("Emil", "Tobias", "Linus")

def my_function(**kid): #dictionary format passing value
    print(kid)

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(food):
    print(food)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)