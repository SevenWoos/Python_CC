# Make serveral dictionaries where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pet_1 = {'name': 'Pal', 
         'animal': 'dog', 
         'owner': 'Arthur'}

pet_2 = {'name': 'Nemo', 
         'animal': 'cat', 
         'owner': 'Francine'}

pets = [pet_1, pet_2]

for pet in pets:
  print(f"\n{pet['name']} is a {pet['animal']}. His owner is {pet['owner']}")