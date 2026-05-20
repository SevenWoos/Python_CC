# Pizza Toppings

prompt = "Please enter a pizza topping: "

while True:
  topping = input(prompt)
  if topping == 'quit':
    break
  else:
    print(f"\nI'll add {topping} to your pizza!")