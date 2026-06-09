import matplotlib.pyplot as plt

from random_walk import RandomWalk

# while True:
  
rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(20, 9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect('equal')

plt.show()
  
  # keep_running = input("Make another walk? (y/n): ")
  # if keep_running == 'n':
  #   break
  