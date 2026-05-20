# Make a list of sandwich_orders and an empty list finished_sandwiches. Loop through each sandwich to simulation completion.

sandwich_orders = ['meatball sub', 'pastrami sandwich', 'turkey sandwich']
finished_sandwiches = []

while sandwich_orders:
  sandwich = sandwich_orders.pop()
  print(f"Making sandwich: {sandwich} ")
  finished_sandwiches.append(sandwich)

# Display all finished sandwiches
print(f"\nHere are all the completed sandwiches: ")
for sandwich in finished_sandwiches:
  print(sandwich)