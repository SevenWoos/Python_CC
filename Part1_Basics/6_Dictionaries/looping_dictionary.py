# We can loop through keys, values, or key-value pairs in a dictionary.
user_0 = {
  'username': 'efermi', 
  'first': 'enrico', 
  'last': 'fermi', 
}
print("Looping through key, value pairs:")
for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")

# We can set the key and value loop values to whatever we want. For example, we can use "name" and "language" if we have a dictionary of programming languages and their creators.
favorite_languages = {
  'jen': 'python', 
  'sarah': 'c',
  'edward': 'rust', 
  'phil': 'python',
}

print("\nLooping through key, value pairs with different variable names:")
for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through just the keys in a dictionary using the keys() method.
print("\nLooping through just the keys:")
for name in favorite_languages.keys():
  print(name.title())

# Looping through the keys and checking if a particular key is in the dictionary, like our friends.
print("\nLooping through the keys and checking if a particular key is in the dictionary:")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")
  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")

# Looping through keys in specific order like sorted.
print("\nLooping through keys in sorted order:")
for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")

# Looping through the values in a dictionary using the values() method.
print("\nLooping through the values:")
print("the following languages have been mentioned:")
for language in favorite_languages.values():
  print(language.title())

# Use a set to avoid duplicates when looping through values.

# When you wrap set() around a list of values, Python identifies the unique items in the list and builds a set from those items.

# A set is a collection in which each item must be unique. When we loop through the set, we see each language listed once, even if it was mentioned by multiple people.
print("\nUsing a set to avoid duplicates when looping through values:")
print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())
