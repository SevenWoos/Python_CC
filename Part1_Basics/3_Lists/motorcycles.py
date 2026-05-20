motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Use append to add an item to the list. Mutates.
motorcycles.append('honda')
print(motorcycles)

# Use insert to insert item at 2nd index. Mutates
motorcycles.insert(1, 'chevy')
print(motorcycles)

# Remove second item. Mutates.
del motorcycles[1]
print(motorcycles)
