# Common error: when prompted for a numerical input, users provide text like words that cannot be converted to integers, instead of numbers. 
# Let's raise a ValueError when this occurs.

def addition():
  print("\nLet's add two numbers: ")
  try:
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")
    value = int(first) + int(second)
  except ValueError:
    print(f"Sorry {first} or {second} is not a valid number!")
  else:
    print(f"\n{value}")

addition()