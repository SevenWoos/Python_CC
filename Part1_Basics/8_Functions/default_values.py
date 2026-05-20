# When writing a function, you can define a default value for each parameter. 
# If an arg is provided in the function call, Python uses the arg value. If not, Python uses the default value.

# Setting a default value for animal_type to "dog".
print("\nSetting a default value for animal_type to 'dog'.")

def describe_pet(pet_name, animal_type='dog'):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('willie')
# When you use default values, any parameter with a default value needs to be listed AFTER all the parameters that don't have default values.
describe_pet(pet_name='harry', animal_type='hamster')

