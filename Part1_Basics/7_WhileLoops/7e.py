# Movie Tickets

prompt = "Welcome to the movies! How old are you? "
while True:
  age = input(prompt)
  if age == 'quit':
    break
  else:
    age = int(age)
    if age <= 3:
      print(f"\nYour ticket is free!")
    elif age <= 12:
      print(f"\nYour ticket is $10.")
    else:
      print(f"\nYour ticket is $15.")
    