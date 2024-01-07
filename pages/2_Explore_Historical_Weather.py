import streamlit as st
from weather_app import api_to_df as api


city_list=['chennai','mumbai','pune','hyderabad','bengaluru','surat','kolkata','ahmedabad','visakhapatnam','madurai']

with st.sidebar:
    histSelectCity = st.sidebar.selectbox(
    "Select the City You want to Explore",
    city_list
    )
    histInputCity = st.text_input("Your city not in List? Please provide it here:")
    st.markdown('**weather data for the city you input here will be stored from this moment')