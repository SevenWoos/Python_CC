# Build a user profile using an arbitrary argument parameter.
def build_profile(first, last, **user_info):
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('peter', 'parker', 
                             superhero_name='Spider-Man', 
                             age=26, 
                             weight=167)
print(user_profile)