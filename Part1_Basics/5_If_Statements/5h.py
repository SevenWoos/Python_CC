users = ['noob', 'admin', 'sven', 'alice', 'bob']

for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Helllo {user}, thank you for logging in again!")