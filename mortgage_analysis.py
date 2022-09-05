import pandas as pd

# function to load 30 to 89 days mortgage deliquent data
def load_30to90_csv():
    late_30to90_days = pd.read_csv('data/MetroAreaMortgagesPercent-30-89DaysLate-thru-2021-12.csv')
    return late_30to90_days

# function to load 90 plus days mortgage deliquent data
def load_90plus_csv():
    late_90plus_days = pd.read_csv('data/MetroAreaMortgagesPercent-90-plusDaysLate-thru-2021-12.csv')
    return late_90plus_days

# function to strip out the year and month columns from dataframe
def get_yearmonth_cols(dataframe):
    year_month_cols = dataframe.columns.difference(['RegionType','Name','CBSACode']).to_list()
    return year_month_cols

# function to group by region
def get_by_region(dataframe,year_month_cols):
    return pd.DataFrame(dataframe.groupby('RegionType').mean().round(2)[year_month_cols].mean(axis=1).round(2).sort_values(ascending=False))

# function to group by region & area name
def get_by_area(dataframe,year_month_cols):
    return pd.DataFrame(dataframe.groupby(['RegionType','Name']).mean().round(2)[year_month_cols].mean(axis=1).round(2).sort_values(ascending=False))
