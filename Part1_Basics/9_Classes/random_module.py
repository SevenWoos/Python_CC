from random import randint

# randint from the "random" module takes 2 integer args and returns a randomly selecte dinteger between those 2 integers and including.

num = randint(1, 6)
print(num)

from random import choice

# choice takes in a list or tuple and returns a randomly chosen element.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)