# Store this function in module called "city_functions.py"

# Create "test_cities.py" to test the function in "city_functions.py"

def city_country(city, country, population=''):
  """Return a string like 'Santiago, Chile'."""
  if population:
    full_city = f"{city}, {country} - {population}"
  else:
    full_city = f"{city}, {country}"
  return full_city.title()