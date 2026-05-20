# ElectricCar inherits from Car class and uses Battery class so remember to import both.
from car import Car
from battery import Battery

# ElectricCar Class
class ElectricCar(Car):
  """Models apsects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)
    self.battery = Battery()

  def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't have a gas tank")