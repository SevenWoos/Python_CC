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

print("\nFirst resturant: ")
in_n_out = Restaurant('In N Out', 'fast food')
print(in_n_out.restaurant_name)
print(in_n_out.cuisine_type)
in_n_out.describe_restaurant()
in_n_out.open_restaurant()
print(in_n_out.number_served)
in_n_out.set_number_served(69)
print(in_n_out.number_served)
in_n_out.increment_number_served(31)
print(in_n_out.number_served)

print("\nSecond resturant: ")
home_eat = Restaurant('HomeEat', 'Chinese')
print(home_eat.restaurant_name)
print(home_eat.cuisine_type)
home_eat.describe_restaurant()
home_eat.open_restaurant()

print("\nThird restaurant: ")
canes = Restaurant("Raising Cane's", 'chicken tenders')
print(canes.restaurant_name)
print(canes.cuisine_type)
canes.describe_restaurant()
canes.open_restaurant()
