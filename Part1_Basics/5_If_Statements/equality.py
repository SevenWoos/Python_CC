# Checking for equality is case sensitive, so 'Audi' and 'audi' are not the same. To make your program more flexible, you can use the lower() method to make the value of car lowercase before you compare it.
print('audi' == 'Audi') # False

car = 'Audi'
print(car.lower() == 'audi') # True
print(car) # Audi

# Check Number Equality
age = 18
print(age == 18) # True