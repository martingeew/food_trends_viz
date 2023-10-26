
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_pickle("../../data/processed/ramen_by_country_12_yr_ma.pkl")

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8.5))

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

# Plotting each country's data with assigned custom colors
for country in data.columns:
    ax.plot(data.index, data[country], label=country, color=country_colors[country])
    
# Set size of plot to accomodate text labels
xmin = data.index.min()
xmax = data.index.max()+ pd.DateOffset(years=2) # add space to the right of the lines for labels
ax.set_xlim(xmin, xmax)

# Define the last value for each country
# LABEL_Y = [data[country].iloc[-1] for country in data.columns]
label_y = {
    "New Zealand": 70.0,
    "Germany": 83.75,  
    "Australia": 75.58, 
    "US": 88.0, 
    "Netherlands": 93.0, 
    "UK": 79.0,  
}

# Set the length for the lines to each label
x_start = data.index.max()
x_end = data.index.max()+ pd.DateOffset(years=1)

# Add labels for countries iteratively
for country in data.columns:
    data_temp = data[[country]].iloc[-1:]
    
    # Country name
    text=country
    
    # Colour for country label
    color = country_colors[country]
    
    # Vertical start of line
    y_start = data_temp.iat[0, 0]
    # Vertical end of line
    y_end = label_y[country]
    
    # Add line based on three points
    ax.plot(
        [x_start, (x_start + (x_end - x_start) / 2) , x_end], 
        [y_start, y_end, y_end], 
        color=color, 
        alpha=0.5, 
        ls="dashed"
    )
    
    # Add country text
    ax.text(
        x_end, 
        y_end, 
        text, 
        color=color, 
        fontsize=14, 
        weight="bold", 
        fontfamily="Montserrat", 
        va="center"
    )


# Setting labels, title, and other properties
ax.set_xlabel('Month')
ax.set_ylabel('12-Month Moving Average of Ramen Interest')
ax.set_title('Ramen Interest Over Time (12-Month Moving Average)')
ax.grid(True)
ax.set_xticks(ax.get_xticks())  # This ensures that the x-ticks are set before rotation
ax.set_xticklabels(ax.get_xticklabels())  # Rotate x-axis labels for better visibility

plt.tight_layout()
plt.show()


