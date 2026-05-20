# Ask for a number and report whether it is a multiple of 10.
number = input("Please enter a number: ")
number = int(number)
if number % 10 == 0:
  print(f"\n{number} is a multiple of 10.")
else:
  print(f"\n{number} is NOT a multiple of 10.")