from restaurant import Restaurant

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