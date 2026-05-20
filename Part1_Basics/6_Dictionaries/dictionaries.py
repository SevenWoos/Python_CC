# Dictionary is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.

# Key's value can be a string, a number, a list, or even another dictionary. 

# You can have an INFINITE number of key-value pairs in a dictionary.

# A simple dictionary to store information about an alien.
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Let's add new key-value pair to the dictionary.
print("\nLet's add new key-value pair to the dictionary.")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting with an empty dictionary.
print("\nStarting with an empty dictionary.")
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values in a dictionary.
print("\nModifying values in a dictionary.")
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


# Modifying the position of the alien based on the speed.
print("\nModifying the position of the alien based on the speed.")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  # This must be a fast alien.
  x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
