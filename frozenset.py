#4 the set and frozen set

# Creating a set

fruits = {"apple", "banana", "cherry", "apple"}
# duplicate apple will be removed
print(fruits)
# output:
# {'banana', 'cherry', 'apple'}

# adding and removing elements

fruits.add("orange")
fruits.remove("cherry")
print(fruits)
# output:
# {'apple', 'banana', 'orange'}

# set operations

fruits2 = {"orange", "mango", "grape"}
print(fruits.union(fruits2))
# output:
# {'grape', 'mango', 'banana', 'apple', 'orange'}

print(fruits.intersection(fruits2))
# output:
# {'orange'}

print(fruits.difference(fruits2))
# output:
# {'banana', 'apple'}   

# FROZENSET:
# creating a frozen set

fruits_frozen = frozenset({"apple", "banana", "cherry", "apple"})
print(fruits_frozen)
# output
# frozenset({'banana', 'apple', 'cherry'})
# frozenset is immutable and cannot be modified

# set operations with frozenset

fruits_frozen2 = frozenset({"orange", "mango", "grape"})
print(fruits_frozen.union(fruits_frozen2))
# output
# frozenset({'orange', 'banana', 'cherry', 'grape', 'apple', 'mango'})

print(fruits_frozen.intersection(fruits_frozen2))
# output
# frozenset()

print(fruits_frozen.difference(fruits_frozen2))
# output
# frozenset({'banana', 'apple', 'cherry'})
