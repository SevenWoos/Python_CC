# Checking against multiple lists.
# Watch for unsual toppings requests that may not be available. In this example, we check the requested toppings against the list of available toppings. If a requested topping is available, we add it to the pizza. If a requested topping is not available, we print a message saying that we are sorry that we don't have that topping. 
# 
# Can also use a tuple for available toppings.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")