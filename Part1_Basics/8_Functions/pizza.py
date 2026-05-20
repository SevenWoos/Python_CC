# First create a module. they must end in ".py"
# EX: pizza.py
# Make sure we remove everyting except this function from the "pizza.py" file
def make_pizza(size, *toppings):
  """Sumamrize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings: ")
  for topping in toppings:
    print(f"- {topping}")