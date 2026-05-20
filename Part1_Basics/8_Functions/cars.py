# Function that stores info about car in a dictionary.
# Function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.

def make_car(manufacturer, model, **car):
  car['manufacturer'] = manufacturer
  car['model'] = model
  return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car2 = make_car('honda', 'accord', color='green', tow_package=True)
print(car2)