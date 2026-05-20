# Create a shirt fucntion that accepts a size and a message.
# Default size is large.
# Default message is "I love Python"
def make_shirt(size='Large', message='I love Python'):
  print(f"Your shirt size is {size}. It has the message: {message}")

make_shirt()
make_shirt(size='Medium')
make_shirt(size='Medium', message='IDK')