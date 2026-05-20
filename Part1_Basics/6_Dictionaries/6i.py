# Make a dictionary called favorite_places. Think of 3 names to use as keys, and store one to three favorite places for each person. Loop through dcitionary and print each name and their favorite places.

favorite_places = {
  'Chandler': ['Taiwan', 'Japan'], 
  'Ross': ['New York', 'Europe'], 
  'Joey': ['Paris', 'San Francisco', 'Los Angeles']
}

for person in favorite_places:
  print(f"\n {person}'s favorite places are: ")
  for place in favorite_places[person]:
    print(f"\t{place}")