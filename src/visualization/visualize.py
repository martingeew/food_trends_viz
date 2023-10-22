
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_pickle("../../data/interim/ramen_data_by_country.pkl")

# Setting 'Month' as the index
data.set_index('Month', inplace=True)

data_moving_avg_12 = data.rolling(window=12).mean()

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

xmin = data_moving_avg_12.index.min().year
xmax = data_moving_avg_12.index.max().year + 4  # Adding 4 years to the maximum year for some padding on the right
#plt.xlim(xmin, xmax)

LABEL_Y = [data_moving_avg_12[country].iloc[-1] for country in data_moving_avg_12.columns]

# Plotting each country's data with assigned custom colors
for country in data_moving_avg_12.columns:
    plt.plot(data_moving_avg_12.index, data_moving_avg_12[country], label=country, color=country_colors[country])

plt.xlabel('Month')
plt.ylabel('12-Month Moving Average of Ramen Interest')
plt.title('Ramen Interest Over Time (12-Month Moving Average)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility, if needed

plt.show()


