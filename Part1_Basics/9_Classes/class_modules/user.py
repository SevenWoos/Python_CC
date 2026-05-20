class User:

  def __init__(self, first_name, last_name, age, weight):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.weight = weight
    self.login_attempts = 0

  def describe_user(self):
    print(f"User's full name is {self.first_name.title()} {self.last_name.title()}.")
    print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old, and weighs {self.weight} lbs.")

  def greet_user(self):
    print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

  def increment_login_attempts(self):
    self.login_attempts += 1
  
  def reset_login_attempts(self):
    self.login_attempts = 0
