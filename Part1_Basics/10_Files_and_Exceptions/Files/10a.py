# Create a "learning_python.txt" file. Write a few lines sumamrizing what I learned in Python.

# Write a program that reads the file and print what I wrote.

# Once by reading in the entire file.

# Once by storing the lines in a list and looping over each line.

from pathlib import Path

print("\nReading in entire file.")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("\nReading in file line by line.")
path = Path('learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
  print(line)
