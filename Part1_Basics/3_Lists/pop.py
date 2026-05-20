# Use pop() if you want to USE the item you remove. pop() removes the LAST item in the list. Mutates.
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yahama', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")