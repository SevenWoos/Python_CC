# Use remove() when you KNOW the value of the item you want to remove.
# remove() tells Python to figure out WHERE the value is first.
# remove() only deletes the FIRST occurrence of a value if it appears multiple times.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

motorcycles = ['honda', 'yahama', 'ducati', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)