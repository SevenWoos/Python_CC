class User:

  def __init__(self, first_name, last_name, age, weight):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.weight = weight
    self.login_attempts = 0

  def describe_user(self):
    print(f"User's full name is {self.first_name.title} {self.last_name.title()}.")
    print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old, and weighs {self.weight} lbs.")

  def greet_user(self):
    print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
  
  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0


class Privileges:

  def __init__(self, privileges):
    self.privileges = privileges

  def show_privileges(self):
    for privilege in self.privileges:
      print(f" - {privilege}")


class Admin(User):

  def __init__(self, first_name, last_name, age, weight):
    super().__init__(first_name, last_name, age, weight)
    self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
  

my_admin = Admin('Nathan', 'Drake', 38, 167)
my_admin.describe_user()
my_admin.greet_user()

my_admin.privileges.show_privileges()
print(my_admin.login_attempts)
my_admin.increment_login_attempts()
my_admin.increment_login_attempts()
my_admin.increment_login_attempts()
print(my_admin.login_attempts)
my_admin.reset_login_attempts()
print(my_admin.login_attempts)