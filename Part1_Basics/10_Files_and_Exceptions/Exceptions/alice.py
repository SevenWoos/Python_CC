# Analyzing Text

# Moving the "alice.txt" into the directory we're working in.

# The split() method splits a string wherever it finds whitespace.

from pathlib import Path

path = Path('alice.txt')
try:
  contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
  print(f"Sorry, the file {path} does not exist.")
else:
  # Count the approximate number of words in the file:
  words = contents.split()
  num_words = len(words)
  print(f"The file {path} has about {num_words} words.")