import plotly.express as px

from die import Die

# Create three D6 dice.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
  result = die_1.roll() + die_2.roll() + die_3.roll()
  results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
  frequency = results.count(value)
  frequencies.append(frequency)
  
# Visualize the results.
title = "Results of Rolling a 3 D6 10000 Times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

fig.show()