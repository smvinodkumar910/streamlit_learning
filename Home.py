import streamlit as st
from weather_app import api_to_df as api
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from weather_app.RealTimeWeather import realTimeWeatherPage
from weather_app.ExploreHistoricalWeather import ExploreHistoricalWeatherPage

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)



authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#hashed_passwords = stauth.Hasher(['k.shanthi910', 'abc']).generate()
    
output = authenticator.login('Login', 'main')


if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    tab1, tab2 = st.tabs(["Real Time Weather", "Historical Weather"])
    with tab1:
        realTimeWeatherPage()

    with tab2:
        ExploreHistoricalWeatherPage()
        
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



with st.container(border=True):
    st.button('New user? Please Register here', on_click=authenticator.register_user('Register','main'))
    
    