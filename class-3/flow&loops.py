#1 control flow & loops
# conditional statements(control flow)

# if statement

x = 12
if x > 8:
    print("x is greater than 8")

# if-else statement

x = 5
if x > 8:
    print("x is greater than 8")
else:
    print("x is less than 8")
x = 5

# if-elif-else statement
if x > 8:
    print("x is greater than 8")
elif x == 5:
    print("x is equal to 8")
else:
    print("x is less than or equal to 8")

# loops in python
# loop through a list

my_list = [11, 22, 33, 44, 55]
for item in my_list:
    print(item)

# loop through a range

for i in range(10):
    print(i)

# while loop

x = 1
while x <= 8:
    print(x)
    x += 1  

# loop control statement
# break statement(stop loop early)

for x in range(20):
    if x == 14:
        break
    print(x)
# brak the loop when x is 14

# continue statement(skips the current iteration)
for x in range(14):
    if x  == 9:
        continue
    print(x)
# skipping 9

# pass statement(does nothing, used AS A PLACEHOLDER)

for x in range(10):
    if x == 5:
        pass
    print(x)
# prints 0 to 4, then skips 5 and prints 6 to 9
