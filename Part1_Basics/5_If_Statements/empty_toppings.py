# Check if list is empty first. Python returns true if the list has at least one item, and false if the list is empty. This is a common way to check for an empty list in Python.

requested_toppings = []

if requested_toppings:
  for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
  print("\nFinished making your pizza!")
else:
  print("Are you sure you want a plain pizza?")

