# Write a program that prompts user for their names in a while loop. Write names to a file called "guest_book.txt".

from pathlib import Path

path = Path('guest_book.txt')
guest_name = ''
while guest_name != 'q':
  guest_name = input("Hello! What is your name: ")
  if guest_name != 'q':
    existing = path.read_text()
    path.write_text(existing + guest_name + "\n")
