# Function that accepts a list of items a person wants on a sandwich.
# Use one parameter in the function

def build_sandwich(*items):
  print("\nHere is what is on the sandwich you built: ")
  for item in items:
    print(f"- {item}")
  print("\n Enjoy!")
build_sandwich('chicken', 'lettuce', 'olives', 'cheese')