# Sometimes you might want to store a dictionary inside a dictionary. This is called nesting. Nesting is a powerful tool that allows you to store complex data structures in a way that is easy to access and manipulate.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Use a list.
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
  print(alien)

# Creating a fleet of aliens.
print("\nCreating a fleet of aliens:")
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

# We can change the first 3 aliens to yellow and medium speed, and give them 10 points each. If they are yellow, change them to red, and change their speed to fast and their points to 15.
for alien in aliens[:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium' 
  elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['points'] = 15
    alien['speed'] = 'fast'

# Show the first 5 aliens.
for alien in aliens[:5]:
  print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


# Nesting a dictionary inside a dictionary.
print("\nNesting a dictionary inside a dictionary:")

users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
  },
}

for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {user_info['location'].title()}")

print("\nTrying to generate different aliens based on divisibility.")
aliens = []
for alien_number in range(30):
  if alien_number % 5 == 0:
    new_alien = {'color': 'red', 'points': 15}
  elif alien_number % 3 == 0:
    new_alien = {'color': 'yellow', 'points': 10}
  else:
    new_alien = {'color': 'green', 'points': 5}
  aliens.append(new_alien)

for alien in aliens:
  print(alien)