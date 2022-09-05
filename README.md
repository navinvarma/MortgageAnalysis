# Mortgage Analysis
## Data
This project uses Consumer Financial Protection Bureau (CPFB) data that is aggregated by state, metro and non-metro areas, and county. Dataset from CPFB which include the full time series and all revisions. These data cover January 2008–December 2021. 

[Data Source](https://www.consumerfinance.gov/data-research/mortgage-performance-trends/download-the-data/)

> These data come from the National Mortgage Database (NMDB), which uses a nationally representative sample of residential mortgages.
> ### Mortgages 30–89 days delinquent
> The 30-89 mortgage delinquency rate is a measure of early stage delinquencies and can be an early indicator of the mortgage market's overall health. It captures borrowers that have missed one or two payments.
> ### Mortgages 90 or more days delinquent
> The 90–day delinquency rate is a measure of serious delinquencies. It captures borrowers that have missed three or more payments. This rate measures more severe economic distress. 

## Technologies 
* Python (Anaconda3) with Vistual Studio as preferred editor
* [*JupyterLab*](https://jupyter.org/install#jupyterlab) for analysis of data to discover trends for mortgages that are deliquent for metro and non-metro regions in the United States of America. 
* Interactive [*StreamLit*](https://streamlit.io/) web application that can accept user input in the future.

## How To
### /mortgage_analysis.py
This file contains the functions to read the CSV data and return dataframes grouped by various columns.

### /mortgage_stats.ipynb
This is a Jupyter Notebook with tables and visualizations of the mortgage data.

To run notebook
```
jupyter lab mortgage_stats.ipynb
```

### /mortgage_analysis_webapp.py
This is a Streamlit page using the same data from the Jupyter Notebook

To run webapp
```
streamlit run mortgage_analysis_webapp.py
```