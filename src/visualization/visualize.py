
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

# Plotting each country's data with assigned custom colors
for country in data.columns:
    plt.plot(data.index, data[country], label=country, color=country_colors[country])

plt.xlabel('Month')
plt.ylabel('12-Month Moving Average of Ramen Interest')
plt.title('Ramen Interest Over Time (12-Month Moving Average)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility, if needed

plt.show()


