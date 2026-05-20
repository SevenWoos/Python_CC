responses = {}

polling_active = True
while polling_active:
  name = input("\nWhat is your name? ")
  response = input("\nWhat is your dream vacation? ")

  responses[name] = response

  repeat = input("\nWould you like to let another person respond? (yes/no)")
  if repeat == 'no':
    polling_active = False

print("\n --- Dream Vacation Polling Results --- ")
for name, response in responses.items():
  print(f"\n{name.title()} would like to go to {response}!")