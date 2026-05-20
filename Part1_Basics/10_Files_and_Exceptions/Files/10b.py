# Use the replace() method to replace every instance of "Python" with "Java".

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
contents = contents.replace('Python', 'Java')
lines = contents.splitlines()
for line in lines:
  print(line)
