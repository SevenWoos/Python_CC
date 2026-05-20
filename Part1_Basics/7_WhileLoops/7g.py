# No Pastrami.

# Remove all instances of pastrami sandwiches.

sandwich_orders = ['meatball sub', 'pastrami', 'turkey sandwich', 'pastrami', 'pastrami', 'meatball sub', 'pastrami']
finished_sandwiches = []

print("\n The deli has run out of pastrami")
while sandwich_orders:
  sandwich = sandwich_orders.pop()
  if sandwich == 'pastrami':
    continue
  else:
    print(f"Making sandwich: {sandwich} ")
    finished_sandwiches.append(sandwich)

# Display all finished sandwiches
print(f"\nHere are all the completed sandwiches: ")
for sandwich in finished_sandwiches:
  print(sandwich)