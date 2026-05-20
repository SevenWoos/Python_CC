# Sometimes we know ahead of time, how many args a function needs to accept. 
# Python has a function that lets you collect an arbitrary number of arguments using the *parameter.

# asterik * in parameter name 'toppings' tells Python to make a TUPLE called "toppings", containing all the values function receives. 
# Python packs the args into a tuple, even if we only have ONE arg.
def make_pizza(*toppings):
  """Print the list of toppings that have been requested."""
  print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("\nReplacing print call with description: ")
def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings: ")
  for topping in toppings:
    print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing arbitrary number of args with positional args.

# Parameter that accepts arbitrary number of args must be placed LAST in the function definition.

# Python matches the positional and keyword args FIRST.
print("\nMixing arbitrary number of args with positional args.")

def make_pizza(size, *toppings):
  """Summarize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings: ")
  for topping in toppings:
    print(f"- {topping}")
make_pizza(16, 'perpperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
