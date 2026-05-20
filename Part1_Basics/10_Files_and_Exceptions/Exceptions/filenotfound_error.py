# FileNotFound Error

# FileNotFound error occurs when we try to read a file that doesn't exist.
# Encoding argument needed when your system's default encoding doesn't match the encoding of the file that's being read.
from pathlib import Path

path = Path('alice.txt')
try:
  contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
  print(f"Sorry, the file {path} does not exist.")
