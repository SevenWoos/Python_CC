# Functions = named blocks of code designed to do 1 job.
def greet_user(username):
  """Display a simple greeting."""
  print(f"Hello, {username.title()}!")
greet_user('jesse')

greet_user('thomas')

# Using positional arguments where order matters.
print("\nUsing positional arguments.")
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Using keyword arguments. A key-value pair that you pass to a function.
print("\nUsing keyword arguments.")
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster', pet_name='harry')
# Order doesn't matter as we can assign the proper values.
describe_pet(pet_name='harry', animal_type='hamster')


# Return Values
print("\nUsing return values")
def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)