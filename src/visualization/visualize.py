
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_pickle("../../data/processed/ramen_by_country_12_yr_ma.pkl")

# change to ax subplot

plt.figure(figsize=(15, 7))  # Adjust the figure size for better visualization

# Define custom colors for each country
country_colors = {
    "New Zealand": "green",  # NZ: green
    "Germany": "black",  # Germany: black
    "Australia": "#DAA520",  # Aus: dark gold
    "US": "blue",  # US: american blue (standard blue used here)
    "Netherlands": "orange",  # Netherlands: Dutch orange (standard orange used here)
    "UK": "red",  # UK: red
    # Add any other countries with their desired colors
}

xmin = data.index.min().year
xmax = data.index.max().year + 4  # Adding 4 years to the maximum year for some padding on the right
#plt.xlim(xmin, xmax)

LABEL_Y = [data[country].iloc[-1] for country in data.columns]

import matplotlib.pyplot as plt

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8.5))

# Plotting each country's data with assigned custom colors
for country in data.columns:
    ax.plot(data.index, data[country], label=country, color=country_colors[country])

# Setting labels, title, and other properties
ax.set_xlabel('Month')
ax.set_ylabel('12-Month Moving Average of Ramen Interest')
ax.set_title('Ramen Interest Over Time (12-Month Moving Average)')
ax.legend()
ax.grid(True)
ax.set_xticks(ax.get_xticks())  # This ensures that the x-ticks are set before rotation
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotate x-axis labels for better visibility

plt.tight_layout()
plt.show()


