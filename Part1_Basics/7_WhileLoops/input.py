# input() function PAUSES program and waits for use to enter some text. Once Python receives the user input, it assigns it to a variable.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("\nPlease enter your name: ")
print(f"\nHello, {name}!")

# You can write a prompt that's longer than one line.
print("\nWriting a prompt longer than one line for an input.")
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")