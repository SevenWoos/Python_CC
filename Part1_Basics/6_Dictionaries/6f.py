favorite_languages = {
  'thomas': 'python', 
  'andrew': 'java',
  'edward': 'rust', 
  'phil': 'python',
}

friends = ['thomas', 'edward']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")
  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")
if 'spongebob' not in favorite_languages.keys():
  print("SpongeBob, please take our poll!")