# Sometimes useful to put a list inside a dictionary. For example, if we want to store pizza toppings for a particular pizza, we can use a list to store those toppings. We can then store that list in a dictionary that describes the pizza.

print("\nUsing a list to store multiple pizza toppings:")
pizza = {
  'crust': 'thick', 
  'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
  print(f"\t{topping}")

print("\nUsing a list to store multiple favorite languages:")
favorite_languages = {
  'jen': ['python', 'ruby'], 
  'sarah': ['c'],
  'edward': ['rust', 'go'], 
  'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")
