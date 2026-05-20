# Create a list of current users and a list of new users. Loop through the new users and check if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.

current_users = ["noob", "bob", "admin", "guest", "billybob"]
new_users = ["Optimus Prime", "megatron", "BOB", "rockhopper", "Admin"]

for new_user in new_users:
  if new_user.lower() in current_users:
    print(f"{new_user.lower()} is already taken, please enter a new username.")
  else:
    print(f"{new_user.lower()} is available!")
