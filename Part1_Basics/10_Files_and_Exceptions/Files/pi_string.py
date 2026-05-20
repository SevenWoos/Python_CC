# Building a single string containing all the digits of pi.

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
  pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))


print("\nReading 1 million digits of pi:")
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
  pi_string += line.lstrip()

# We'll just print the first 50 decimal places.
print(f"{pi_string[:52]}...")
print(len(pi_string))