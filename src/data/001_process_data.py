import pandas as pd

# --------------------------------------------------------------
# 1. Define objective
# --------------------------------------------------------------

""" 
The objective of this script is to create a dataset of ramen google trends
by country.

Figures
- 
- 

"""

# --------------------------------------------------------------
# 2. Read raw data
# --------------------------------------------------------------

# Loading all the datasets using the provided format
aus_ramen_df = pd.read_csv('../../data/raw/aus_ramen.csv', parse_dates=[0], index_col=[0], skiprows=1)
germany_ramen_df = pd.read_csv('../../data/raw/germany_ramen.csv', parse_dates=[0], index_col=[0], skiprows=1)
nth_ramen_df = pd.read_csv('../../data/raw/nth_ramen.csv', parse_dates=[0], index_col=[0], skiprows=1)
nz_ramen_df = pd.read_csv('../../data/raw/nz_ramen.csv', parse_dates=[0], index_col=[0], skiprows=1)
uk_ramen_df = pd.read_csv('../../data/raw/uk_ramen.csv', parse_dates=[0], index_col=[0], skiprows=1)
us_ramen_df = pd.read_csv('../../data/raw/US_ramen.csv', parse_dates=[0], index_col=[0], skiprows=1)


# --------------------------------------------------------------
# 3. Process data
# --------------------------------------------------------------

# Resetting the index to make 'Month' a column
datasets = [
    aus_ramen_df.reset_index(), 
    germany_ramen_df.reset_index(), 
    nth_ramen_df.reset_index(), 
    nz_ramen_df.reset_index(), 
    uk_ramen_df.reset_index(), 
    us_ramen_df.reset_index()
]

# Merging all datasets on 'Month' column using pd.merge
merged_df = datasets[0]  # Initialize with the first dataset
for df in datasets[1:]:  # Iterate over the rest of the datasets
    merged_df = pd.merge(merged_df, df, on='Month', how='outer')


# Rename columns
rename_columns = {
    "ramen: (Australia)": "Australia",
    "ramen: (Germany)": "Germany",
    "ramen: (Netherlands)": "Netherlands",
    "ramen: (New Zealand)": "New Zealand",
    "ramen: (United Kingdom)": "UK",
    "ramen: (United States)": "US"
}
merged_df.rename(columns=rename_columns, inplace=True)


# --------------------------------------------------------------
# Export
# --------------------------------------------------------------

merged_df.to_pickle("../../data/interim/ramen_data_by_country.pkl")
