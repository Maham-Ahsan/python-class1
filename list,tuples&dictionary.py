# Lists, Tuples and Dictionaries
# LIST(mutable- can be changed)
# creating a list
colours = ["red" , "orange", "green", "yellow"]
print(colours)
# output:
# ['red', 'orange', 'green', 'yellow']

# Accessing elements
print(colours[0])   
# first element
print(colours[-1])
# last element
# output:
# red
# yellow

# modifying a list

colours.append("blue")
colours.remove("orange")
print(colours)
# output:
# ['red', 'green', 'yellow', 'blue']

# TUPLE (immutable - connot be changed)
fruits = ("apple", "banana", "cherry")
print(fruits)
# output:
# ('apple', 'banana', 'cherry')

# accessing elements

print(fruits[1])
# output
# banana

# DICTIONARY (key-value pairs)
# creating a dictionary

my_info = {
    "name": "ali",
    "age": 30,
    "city": "pakistan"
}
print(my_info)
# output:
# {'name': 'ali', 'age': 30, 'city': 'pakistan'}

# accessing elements

print(my_info["name"])
# output:
# ali

# adding and modifying a dictionary

my_info["address"] = "123 Main St"
my_info["grade"] = "A"
print(my_info)
 # output:
 # {'name': 'ali', 'age': 30, 'city': 'pakistan', 'address': '123 Main St', 'grade': 'A'}