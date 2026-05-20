# Wrap code in a while loop, and continue entering numbers, even if they make a mistake and enter text instead of a number.

def addition():
  while True:
    print("\nLet's add two numbers: ")
    try:
      first = input("Enter the first number: ")
      if first == 'q':
        break
      second = input("Enter the second number: ")
      if second == 'q':
        break
      value = int(first) + int(second)
    except ValueError:
      print(f"Sorry {first} or {second} is not a valid number!")
    else:
      print(f"\n{value}")

addition()