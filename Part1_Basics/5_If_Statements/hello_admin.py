users = ['noob', 'admin', 'dave', 'alice', 'bob']

if users:
  for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Helllo {user}, thank you for logging in again!")
else:
    print("We need to find some users!")

print("\n")

users = []
if users:
  for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Helllo {user}, thank you for logging in again!")
else:
    print("We need to find some users!")
