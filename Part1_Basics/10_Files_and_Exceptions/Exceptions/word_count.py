# Adding more books to analyze.

from pathlib import Path

def count_words(path):
  """Count the approximate number of words in a file."""
  try:
    contents = path.read_text(encoding='utf-8')
  except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
    # Run "pass" if we want the except block to do nothing
    # pass
  else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# path = Path('alice.txt')
# count_words(path)

# Intentionally left out 'siddhartha.txt' to handle a FileNotFound exception.
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
  path = Path(filename)
  count_words(path)