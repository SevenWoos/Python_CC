# Function can return any type of value like a dictionary.
def build_person(first_name, last_name):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Do the same with optional values.
def build_person(first_name, last_name, age=None):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  if age:
    person['age'] = age
  return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
