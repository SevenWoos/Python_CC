# Tuples = immutable list.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# Trying to change a tuple's value.
# dimensions[0] = 250

# Looping through all values in a tuple
print('\n')
my_tuple = (1, 2, 3, 4, 5)
for num in my_tuple:
    print(num)

# Using range() to create a tuple of numbers.
new_tuple = tuple(range(1, 11))
for num in new_tuple:
    print(num)
