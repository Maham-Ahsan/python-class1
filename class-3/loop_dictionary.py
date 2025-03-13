#2 loop through a dictionary
# loop through keys

my_info = {"name": "ali", "age": 30, "city": "Pakistan"}
for key in my_info:
    print(key)
# output:
# name
# age
# city

# loop through values

for value in my_info.values():
    print(value)
# output:
# ali
# 30
# Pakistan

# loop through key-value pairs

for key, value in my_info.items():
    print(f"{key}: {value}")
# output:
# name: ali
# age: 30
# city: Pakistan

# # loop through keys in sorted order

for key in sorted(my_info):
    print(f"{key}: {my_info[key]}")
# output:
# age: 30
# city: Pakistan
# name: ali