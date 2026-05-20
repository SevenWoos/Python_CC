from car import Car
from electric_car import ElectricCar

# using alias
# from electric_car import ElectricCar as EC
# import electric_car as ec

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
