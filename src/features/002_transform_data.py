import pandas as pd


data = pd.read_pickle("../../data/interim/ramen_data_by_country.pkl")

# --------------------------------------------------------------
# Transform data
# --------------------------------------------------------------

# Setting 'Month' as the index
data.set_index('Month', inplace=True)

data_moving_avg_12 = data.rolling(window=12).mean()

# --------------------------------------------------------------
# Export data
# --------------------------------------------------------------

data_moving_avg_12.to_pickle("../../data/processed/ramen_by_country_12_month_ma.pkl")
