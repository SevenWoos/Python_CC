# Using a dictionary to store people's favorite languages.

# Good practice to break larger dictionary into multiple lines for better readability.

# Also good practice to include a comma after the last key-value pair, so that if we add more key-value pairs later, we won't forget to add a comma to the previous line.

favorite_languages = {
  'jen': 'python', 
  'sarah': 'c', 
  'edward': 'rust',
  'phil': 'python',
}

print("\nLooking up values in the dictionary.")
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
