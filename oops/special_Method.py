class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1)  # Output: Alice is 25 years old
print(person2)  # Output: Bob is 30 years old

print(repr(person1))  # Output: Person('Alice', 25)
print(repr(person2))  # Output: Person('Bob', 30)

print(person1 == person2)  # Output: False
print(person1 == Person("Alice", 25))  # Output: True

print(person1 < person2)  # Output: True
print(person2 < person1)  # Output: False
