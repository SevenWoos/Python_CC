# Make 3 new dictionaries representing different trains. Store 3 dictionaries in a list called trains. Loop through your list of trains and print everything you know about each train.

train_2 = {'name': 'Edward', 
           'number': 2, 
           'year': 1945}
train_3 = {'name': 'Henry', 
           'number': 3, 
           'year': 1945}
train_4 = {'name': 'Gordon', 
           'number': 4, 
           'year': 1945}

trains = [train_2, train_3, train_4]

for train in trains:
  print(f"\nTrain name: {train['name']}")
  print(f"Train number: {train['number']}")
  print(f"Train year: {train['year']}")