from admin import Admin

my_admin = Admin('Nathan', 'Drake', 38, 167)
my_admin.describe_user()
my_admin.greet_user()

my_admin.privileges.show_privileges()
print(my_admin.login_attempts)
my_admin.increment_login_attempts()
print(my_admin.login_attempts)
my_admin.reset_login_attempts()
print(my_admin.login_attempts)
