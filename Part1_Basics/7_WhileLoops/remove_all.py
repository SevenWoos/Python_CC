# Use a while loop to remove ALL instances of a value in a list.
# Example: remove all instances of 'cat'.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
  pets.remove('cat')
print(pets)