favorite_places = {
  'Chandler': ['Taiwan', 'Japan'], 
  'Ross': ['New York', 'Europe'], 
  'Joey': ['Paris', 'San Francisco', 'Los Angeles']
}

for person in favorite_places:
  print(f"\n {person}'s favorite places are: ")
  for place in favorite_places[person]:
    print(f"\t{place}")