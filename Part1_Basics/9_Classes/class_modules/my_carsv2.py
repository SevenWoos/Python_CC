# Version that imports the ENTIRE cars module.
# We have to use the "car.Car" and "car.ElectricCar" syntax
import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())