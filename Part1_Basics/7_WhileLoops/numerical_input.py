# When using the input() function, Python interpets everything as a STRING.
# String representation of number is returned.
age = input("How old are you? ")
print(age)

# We cannot run numerical operations.
# print(age >= 18)

# Resolve issue with int() function.
print("\nUsing the int() function")
age = input("How old are you? ")
age = int(age)
print(age >= 18)

# Rollercoaster example
print("\nRollercoaster example.")
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're a little older.")