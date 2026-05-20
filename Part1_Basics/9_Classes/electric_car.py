# Car class
class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    # Set a default value
    self.odometer_reading = 0

  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """Print a statement showing the cars' mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")
  
  # We can modify an attribute's value through a method.
  def update_odometer(self, mileage):
    """Set the odometer reading to the given value.
    Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increase_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

  def fill_gas_tank(self):
    print("Filling up the car!")

# Battery Class
class Battery:
  """A simple attempt to model a battery for an electric car."""

  def __init__(self, battery_size=40):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size

  def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kwh battery.")     

  def get_range(self):
    """Print a statement about the range this battery provides."""
    if self.battery_size == 40:
      range = 150
    elif self.battery_size == 65:
      range = 225
    
    print(f"This car can go about {range} miles on a full charge.")

  def upgrade_battery(self):
    if self.battery_size < 65:
      self.battery_size = 65
    else:
      print(f"Battery capacity has been upgraded to the max!")
  

# ElectricCar class that inherits from Car class.
class ElectricCar(Car):
  """Represents apsects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)
    self.battery = Battery()
    # self.battery = Battery(50)

  # Override this method from Car

  def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't have a gas tank")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()