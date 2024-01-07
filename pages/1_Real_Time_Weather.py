import streamlit as st
from weather_app import api_to_df as api
import requests
from PIL import Image



city_list=['chennai','mumbai','pune','hyderabad','bengaluru','surat','kolkata','ahmedabad','visakhapatnam','madurai']

with st.sidebar:
    selectCity = st.sidebar.selectbox(
    "Select the City You want to Explore",
    city_list
    )
    inputCity = st.text_input("Your city not in List? Please provide it here:",value="")

if inputCity=="":
    wd_df, loc_df, cc_df = api.get_weather(selectCity)
    city = selectCity
else:
    wd_df, loc_df, cc_df = api.get_weather(inputCity)
    city = inputCity

# City details container
cr1 =st.container(border=True)
cr1.header('Weather of the city '+loc_df['name'][0])
cr1.text(loc_df['region'][0] +', '+loc_df['country'][0])
icon_url = cc_df['icon'][0]

col1, col2 = cr1.columns(spec=[0.1,0.9],gap="small")
with col1:
    st.image(Image.open(requests.get('https:'+icon_url, stream=True).raw), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

with col2:
    st.subheader(cc_df['text'][0])
    daystring = ' Night' if wd_df['is_day'][0]==0 else 'Day'
    st.text(  daystring +' at local time '+loc_df['localtime'][0]+' '+loc_df['tz_id'][0])


# Map container
cr2 =st.container(border=True)
cr2.map(loc_df,latitude='lat',longitude='lon')



# Map container
cr3 =st.container(border=True)

radio1 = cr3.radio('Unit',options=['Celcius','Farenheit'],horizontal=True)


tempslider1 = cr3.slider('Temperature',min_value=0.0,max_value=100.0,value=float(wd_df['temp_c'][0]),step=5.0,disabled=True)

tempslider2 = cr3.slider('Temperature Feels Like',min_value=0.0,max_value=100.0,value=float(wd_df['feelslike_c'][0]),step=5.0,disabled=True)


wd_df['temp_c'][0]
wd_df['temp_f'][0]
wd_df['pressure_mb'][0]
wd_df['pressure_in'][0]
wd_df['humidity'][0]
wd_df['cloud'][0]
wd_df['feelslike_c'][0]
wd_df['feelslike_f'][0]






