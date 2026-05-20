# Using get() to access values in a dictionary.

# Using keys in square brackets to access values in a dictionary works well as long as the key exists. If we try to access a value using a key that does NOT exist, Python will raise a KeyError.
print("Raises a KeyError because 'points' is not a key in the dictionary.")
alien_0 = {'color': 'green', 'speed': 'slow'}
# This will raise a KeyError because 'points' is not a key in the dictionary.
# print(alien_0['points'])


# Using get() to set a default value to be returned, if the requested key does NOT exist.

# If we leave out the second parameter in get(), Python will return None if the requested key is not found. 
# None is a special value that Python uses to indicate the absence of a value. It's similar to null in other programming languages.
print("\nUsing get() to set a default value to be returned, if the requested key does NOT exist.")
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)