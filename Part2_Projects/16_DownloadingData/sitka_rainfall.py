from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Preview header.
# print(header_row)

# Extract dates and precipitation.
dates, precipitation = [], []

for row in reader:
  current_date = datetime.strptime(row[2], '%Y-%m-%d')
  try:
    rain = float(row[5])
  except ValueError:
    print(f"Missing data for {current_date}")
  else:
    dates.append(current_date)
    precipitation.append(rain)
    
# Plot the precipitations for 2021.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precipitation, color='blue')

# Format Plot.
title = "Daily Precipitation Levels, 2021 \nSitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation Levels', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
