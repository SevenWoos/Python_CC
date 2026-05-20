# Make a copy of a list using [:]

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


# Adding a new food to each list to prove they are SEPARATE lists.
print('\n')
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)