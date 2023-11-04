
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot_utils import save_plot_as_image

data = pd.read_pickle("../../data/processed/ramen_by_country_12_month_ma.pkl")

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8.5))

# --------------------------------------------------------------
# Set styling
# --------------------------------------------------------------

# Colour pallete
GREY10 = "#1a1a1a"
GREY30 = "#4d4d4d"
GREY40 = "#666666"
GREY50 = "#7f7f7f"
GREY60 = "#999999"
GREY75 = "#bfbfbf"
GREY91 = "#e8e8e8"
GREY98 = "#fafafa"

CORAL = "#E63946"
TURQUOISE = "#2A9D8F"
GOLD = "#DAA520"
PURPLE = "#5A189A"
TEAL = "#1B7B7E"
ROSE = "#FF4C29"
SIENNA = "#985F6F"
BLUE = "#0077B6"
PEACH = "#FFAD69"
SKY = "#8ACBF7"
MUTED_BLACK = "#2C2C2C"
SUNSET_ORANGE = "#FC8D62"
CHARCOAL = "#333333"

# Set background colours
fig.patch.set_facecolor(GREY98) # sets colour of entire background (incl. outside the plot area)
ax.set_facecolor(GREY98) # set colour of plot area

# Customize spines
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["bottom"].set_color("none")

ax.set_xticks(ax.get_xticks())  # This ensures that the x-ticks are set before rotation

ax.set_xticklabels(ax.get_xticklabels())  # Rotate x-axis labels for better visibility

# Set tick label font size to 12pt
ax.tick_params(axis='both', which='major', labelsize=16)

# Set tick color for the x-axis
ax.tick_params(axis='x', colors=GREY40)

# Remove ticks and labels for the y-axis
ax.tick_params(axis='y', left=False, labelleft=True)

# Set font family
#font_family='Corbel'
font_family='Consolas' # techy feel
#font_family='Comic Sans MS' # very casual
#font_family='Candara' # sans-serif but more rounded



# --------------------------------------------------------------
# Create line plot with annotated labels
# --------------------------------------------------------------

# Define custom colors for each country
country_colors = {
    "New Zealand": MUTED_BLACK,
    "Germany": GOLD,
    "Australia": SKY,
    "US": BLUE,
    "Netherlands": SUNSET_ORANGE,
    "UK": CORAL
}


# Plotting each country's data with assigned custom colors
for country in data.columns:
    ax.plot(data.index, data[country], label=country, color=country_colors[country],linewidth=3)
    
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
        fontsize=15, 
        weight="bold", 
        fontfamily=font_family, 
        va="center"
    )
    
# --------------------------------------------------------------
# Plot specific customizations
# --------------------------------------------------------------

# Define the start, end, and frequency of the x tick labels
start = '2005-01-01'
end = '2025-01-01'
frequency = '24M'  # Every 2 years
x_tick_labels = pd.date_range(start=start, end=end, freq=frequency)

ax.set_xticks(x_tick_labels)
ax.set_xticklabels(x_tick_labels.strftime('%Y'), weight=500,
    color=GREY40, fontfamily=font_family) 

# Customize the start, end, and frequency of the horizontal grid lines
y_start = 0.0
y_end = 100
y_frequency = 10
y_ticks = np.arange(y_start, y_end + y_frequency, y_frequency)
y_ticks = np.round(y_ticks).astype(int)

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks, weight=500,
    color=GREY40,fontfamily=font_family) 

ax.grid(True, axis='y', color=GREY91, lw=1.0)  # Ensure the horizontal grid is enabled

fig.suptitle(
    'Google searches for Ramen in selected countries',
    fontsize=30, 
    x=0.045, # set padding on the left of the heading
    ha='left',
    color=CHARCOAL, 
    fontfamily=font_family,
    weight="bold", 
    )

ax.set_title(
    '12-month moving average, 2004-2023 (100 = peak popularity)',
    loc='left',
    fontsize=18,
    pad=24,
    color=CHARCOAL,
    fontfamily=font_family
    )

ax.annotate(
    '@mardywong',
    xy = (1.0, -0.15),
    xycoords='axes fraction',
    ha='right',
    va="center",
    fontsize=14,
    fontfamily=font_family
)

ax.annotate(
    'Source: Google trends',
    xy = (0.0, -0.15),
    xycoords='axes fraction',
    ha='left',
    va="center",
    fontsize=14,
    fontfamily=font_family
)

plt.tight_layout()
save_plot_as_image(filename='ramen_trend_by_country') # Save the image into a folder
plt.show()
