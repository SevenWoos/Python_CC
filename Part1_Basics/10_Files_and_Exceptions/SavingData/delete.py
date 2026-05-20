from pathlib import Path
import json

def get_stored_user_info(path):
  if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    return user_info
  else:
    return None
  
def get_new_user_info(path):
  username = input("What is your name? ")
  age = input("How old are you? ")
  location = input("What state do you live in? ")

  user_info = {'username': username, 
               'age': age, 
               'location': location}
  contents = json.dumps(user_info)
  path.write_text(contents)
  return user_info

def greet_user():
  path = Path('user_dictionary.json')
  user_info = get_stored_user_info(path)
  if user_info:
    confirm = input(f"Are you {user_info['username']}? (yes/no): ")
    if confirm.lower() == 'yes':
      print(f"Welcome back, {user_info['username']}!")
      print(f"You are {user_info['age']} years old and live in {user_info['location']}!")
    else:
      user_info = get_new_user_info(path)
      print(f"We'll remember you when you come back, {user_info['username']}!")

  else:
    user_info = get_new_user_info(path)
    print(f"We'll remember you when you come back, {user_info['username']}!") 

greet_user()