# When we no longer need a key-value pair in a dictionary, we can use the del statement to remove the key-value pair. The del statement deletes the key and its associated value PERMANENTLY.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

print("\nDeleting the key-value pair 'points'.")
del alien_0['points']
print(alien_0)

