import streamlit as st

from components.graphs import plot_geo_with_size, plot_geo_with_size_and_year, plot_geo_with_size_and_year_log
from components.data_engg import load_data_and_clean_data   

df = load_data_and_clean_data()

st.subheader('Meteorite Landings across the globe with size of meteorite (in kg) as size of the bubble')

st.plotly_chart(plot_geo_with_size(df))

st.subheader('Meteorite Landings across the globe with size of meteorite (in kg) as size of the bubble and year as animation')

st.plotly_chart(plot_geo_with_size_and_year(df))

st.subheader('Meteorite Landings size of meteorite (in kg) vs year')
st.plotly_chart(plot_geo_with_size_and_year_log(df))