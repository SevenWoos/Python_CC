# Sort list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sort list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorted() sorts TEMPORARILY.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

print(len(cars))