# Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
from random import choice

lottery_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']
lottery_ticket = ''

for i in range(4):
  random_value = str(choice(lottery_values))
  lottery_ticket += random_value

print(f"\nThe winning lottery ticket is: {lottery_ticket}!")

def select_ticket():
  lottery_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd']
  lottery_ticket = ''
  for i in range(4):
    random_value = str(choice(lottery_values))
    lottery_ticket += random_value
  return lottery_ticket

# Brute forcing the lottery ticket numbers until we win.

def brute_force(winning_ticket):
  attempts = 1
  our_ticket = select_ticket()
  while our_ticket != winning_ticket:
    our_ticket = select_ticket()
    attempts+=1
  print(f"Matched after {attempts} attempts!")

brute_force(lottery_ticket)

# First time running
# The winning lottery ticket is: c93a!
# Matched after 56347 attempts!