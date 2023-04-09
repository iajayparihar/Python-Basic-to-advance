class MyClass:
    def __init__(self):
        self.__private_var = 10

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        self.__private_method()
        print("This is a public method.")

obj = MyClass()
obj.public_method()
# we can not directly access the __private_method that why we use the public method to call that private method
