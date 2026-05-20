# While Loops keep running as long as you want it to keep playing like games.

# Use a while loop to count through a series of numbers.
current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

print("\nLetting the user choose when to end while loop.")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# Set message to empty, so Python has something to check the first time it runs the while loop.
message = ""
while message != 'quit':
  message = input(prompt)
  if message != 'quit':
    print(message)
