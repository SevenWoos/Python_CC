# Ask for number of people for resturant seating. If greater than 8, make them wait.
seats = input("How many people are in your dinner group? ")
seats = int(seats)
if seats > 8:
  print("\nYou'll have to wait for an open table.")
else:
  print(f"\nYour table for {seats} is ready!")
