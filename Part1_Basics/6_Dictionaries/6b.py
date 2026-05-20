# Use dictionary to store people's favorite numbers. Print each person's name and number.
favorite_numbers = {'Thomas': 1, 
                    'Edward': 2, 
                    'Henry': 3, 
                    'Gordon': 4, 
                    'James': 5, 
                    'Percy': 6, 
                    'Toby': 7, 
                    'Duck': 8, }

for name, number in favorite_numbers.items():
  print(f"{name}'s favorite number is {number}.")
