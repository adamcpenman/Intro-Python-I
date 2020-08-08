"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for x in range(5):
    y.append(x + 1)

print("for loop")
print(y)
#[1, 2, 3, 4, 5]

# List comprehension
y = [x for x in range(1, 6)]
print("List comprehension")

print(y)

print("-----------" * 4)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for x in range(10):
    y.append(x**3)


print("for loop")
print(y)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x**3 for x in range(10)]
print("List comprehension")
print(y)

print("-----------" * 4)

# # Write a list comprehension to produce the uppercase version of all the
# # elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []
for x in a:
    y.append(x.upper())
print("for loop")
print(y)


print("List comprehension")
y = [x.upper() for x in a]
print(y)

print("-----------" * 4)

# # Use a list comprehension to create a list containing only the _even_ elements
# # the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
print(x)
# # What do you need between the square brackets to make it work?

# creating a loop to loop through x
# added an if statement to check what numbers that were inputted are divisible by 2
y = [z for z in x if int(z) % 2 == 0]

print("EVENS")

print(y)
