# Break lets you exit a while loop immediately without having to run any of the remaining code in the loop.

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I'd love to go to {city.title()}!")
  
print("\n Break in numbers while loop example.")
i = 0
while True:
  i+=1
  if i == 4: 
    break
  else:
    print(i)