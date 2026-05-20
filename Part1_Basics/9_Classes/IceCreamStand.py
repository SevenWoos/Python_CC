# Create IceCreamStand class that inherits from Restaurant class.

# Parent class Restaurant
class Restaurant:

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0
  
  def describe_restaurant(self):
    print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
  
  def open_restaurant(self):
    print(f"{self.restaurant_name} is open!")

  def set_number_served(self, number):
    self.number_served = number

  def increment_number_served(self, number):
    self.number_served += number

# Child class IceCreamStand inherits from Restaurant
class IceCreamStand(Restaurant):

  def __init__(self, restaurant_name, cusine_type, flavors):
    super().__init__(restaurant_name, cusine_type)
    self.flavors = flavors
  
  def display_flavors(self):
    print("\nHere are all the ice cream flavors available at this stand: ")
    for flavor in self.flavors:
      print(f"- {flavor}")

baskin_robbins = IceCreamStand('Baskin Robbins', 'ice cream',  ['chocolate', 'mint chocolate chip', 'vanilla'])
baskin_robbins.describe_restaurant()
baskin_robbins.open_restaurant()
baskin_robbins.display_flavors()
