# We can store our functions in a separate file called a module.

# We can then IMPORT that module into our main program.

# First create a module. they must end in ".py"
# EX: pizza.py
# Make sure we remove everyting except this function from the "pizza.py" file
def make_pizza(size, *toppings):
  """Sumamrize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings: ")
  for topping in toppings:
    print(f"- {topping}")

# Now we will make a SEPARATE file called "making_pizzas.py" in the same directory as "pizza.py". This file imports the module and then makes two calls to make_pizza().

# "import pizza" opens "pizza.py" and copies over all functions from it into the "make_pizza" program.

# "import" will get EVERY function from the module and make them available to our program.

# We can import a specific function from a module.
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# We can import a function with an alias
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')