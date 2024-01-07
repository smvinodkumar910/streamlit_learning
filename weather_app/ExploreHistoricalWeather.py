import streamlit as st
from weather_app import api_to_df as api


city_list=['chennai','mumbai','pune','hyderabad','bengaluru','surat','kolkata','ahmedabad','visakhapatnam','madurai']

def ExploreHistoricalWeatherPage():
    
    st.markdown('**weather data for the city you input here will be stored from this moment')