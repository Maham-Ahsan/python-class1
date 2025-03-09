# Identity Operators

# Identity operator checks if the memory locations of two objects are the same.

# Syntax: variable1 is variable2

# Example:

x = 5
y = x

print(x is y)  
# Output: True

# Using the id() function to get the memory location of an object

print(id(x))  
# Output: 140709230291040
print(id(y))  
# Output: 140709230291040

# Using the is not operator

print(x is not y)  # Output: False

# Using the type() function to get the type of an object

print(type(x))  
# Output: <class 'int'>
print(type(y))  
# Output: <class 'int'>

# Using the isinstance() function to check if an object is an instance of a class

class Animal:
    pass

class Dog(Animal):
    pass

animal = Animal()

print(isinstance(animal, Animal))  
# Output: True