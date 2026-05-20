# Use series of multiple if statements to check for multiple toppings. This is because the if else chain will stop checking after the first condition is met, so if we want to check for multiple toppings, we need to use multiple if statements instead of an if else chain.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")