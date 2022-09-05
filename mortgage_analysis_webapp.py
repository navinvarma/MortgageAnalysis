import streamlit as st
import mortgage_analysis

st.title('Mortgage Analysis')
late_30to90_days = mortgage_analysis.load_30to90_csv()
late_90plus_days = mortgage_analysis.load_90plus_csv()
year_month_cols = mortgage_analysis.get_yearmonth_cols(late_30to90_days)
late_30to90_days_region = mortgage_analysis.get_by_region(late_30to90_days, year_month_cols)
late_90plus_days_region = mortgage_analysis.get_by_region(late_90plus_days, year_month_cols)
late_30to90_days_area = mortgage_analysis.get_by_area(late_30to90_days, year_month_cols)
late_90plus_days_area = mortgage_analysis.get_by_area(late_90plus_days, year_month_cols)

st.subheader('Raw Data: Mortgages Late by 30 to 89 days')
st.write(late_30to90_days)

st.subheader('Raw Data: Mortgages Late by 90+ days')
st.write(late_90plus_days)

