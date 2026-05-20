# Ordinal numbers are numbers that indicate the position of something in a list, such as 1st, 2nd, 3rd, etc. In this code, we will create a list of ordinal numbers from 1 to 9 and print them with their appropriate suffixes.

numbers = list(range(1, 10))
for number in numbers:
  if number == 1:
    print(f"{number}st")
  elif number == 2:
    print(f"{number}nd")
  elif number == 3:
    print(f"{number}rd")
  else:
    print(f"{number}th")
