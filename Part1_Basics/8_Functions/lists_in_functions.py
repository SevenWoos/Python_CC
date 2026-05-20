# We have a list of users and want to print a greeting for each.
def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = f"Hello, {name.title()}"
    print(msg)
  
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# When you pass a list to a function, the function can MODIFY the list permanently.
