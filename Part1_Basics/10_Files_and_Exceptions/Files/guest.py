# Write a program that prompts user for their name. Write name to a file called "guest.txt".

from pathlib import Path

path = Path('guest.txt')
guest_name = input("Hello! What is your name: ")
path.write_text(guest_name)
