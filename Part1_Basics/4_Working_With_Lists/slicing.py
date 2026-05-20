lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lst[0:5])

print('\n')

print(lst[1:5])

print('\n')

# Leaving first value blank, slices from beginning of list.
print(lst[:6])

print('\n')

# Leaving last value blank, slices all the way to the end of the list.
print(lst[2:])

print('\n')

# Output specific number of end values with a negative number.
# Get last 3 numbers
print(lst[-3:])

print('\n')

# Looping through a slice.
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first 3 players on my team: ")
for player in players[:3]:
    print(player.title())
