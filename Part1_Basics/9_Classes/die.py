from random import randint

class Die:

  def __init__(self, sides):
    self.sides = sides

  def roll_dice(self):
    result = randint(1, self.sides)
    print(result)

print("\n Create six-sided die.")
six_sides = Die(6)
six_sides.roll_dice()

print("\n Create ten-sided die and roll it 10 times.")
ten_sides = Die(10)
for i in range(10):
  ten_sides.roll_dice()

print("\n Create twenty-sided die and roll it 10 times.")
twenty_sides = Die(20)
for i in range(10):
  twenty_sides.roll_dice()