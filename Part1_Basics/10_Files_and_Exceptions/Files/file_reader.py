from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

print("\nUsing splitlines() to split by lines.")
lines = contents.splitlines()
for line in lines:
  print(line)