# Sometimes you'll want to accept an arbitrary number of args, BUT you don't know what kind of info will be passed in.

# Building a user profile, but we don't know what kind of info we'll get.
# In our example, we expect a first name and a last name. We then allow the user to pass in as many key-value pairs as they want.
def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton', 
                             field='physics')
print(user_profile)