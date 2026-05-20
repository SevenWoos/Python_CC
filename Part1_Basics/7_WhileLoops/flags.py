# What do we do when we have more complicated programs, where MANY different events could cause the program to stop running? Trying to test ALL conditions under one while loop, becomes COMPLEX.

# Example, in a game, many events could cause the game to end. Losing lives, time running out, etc.

# Use a flag.

# Flag is a variable that acts as a signal to the program as to whether or not the entire program is active.

# We can set our flag to True while running the loop, and stop running when any of the stopping conditions occur by setting the flag to False.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message)
