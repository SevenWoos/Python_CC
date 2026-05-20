from user import User
from privileges import Privileges

# Child class Admin that inherits from User.
class Admin(User):

  def __init__(self, first_name, last_name, age, weight):
    super().__init__(first_name, last_name, age, weight)
    self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])

  