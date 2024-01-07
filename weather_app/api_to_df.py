import requests
import pandas as pd
from datetime import datetime as dt
import pytz
import os
from io import BytesIO


def get_weather(city:str):

    city_list=[city]


    url = "https://weatherapi-com.p.rapidapi.com/current.json"



    headers = {
        "X-RapidAPI-Key": "11e969206dmsh2dc567692521a17p1aff25jsnf8d1e65d23f9",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    location=[]
    weather_details=[]
    current_condition=[]

    for city in city_list:
        querystring = {"q":city}
        response = requests.get(url, headers=headers, params=querystring)
        output = response.json()
        loc=output.get("location")
        cc = output.get("current").get("condition")
        wd = output.get("current")

        del wd['condition']
        wd['city']=loc.get("name")

        cc['weather_time'] = wd.get("last_updated")
        cc['city'] = loc.get("name")
        
        location.append(loc)
        current_condition.append(cc)
        weather_details.append(wd)


    loc_df = pd.DataFrame(location)
    cc_df = pd.DataFrame(current_condition)
    wd_df = pd.DataFrame(weather_details)

    return wd_df, loc_df, cc_df
