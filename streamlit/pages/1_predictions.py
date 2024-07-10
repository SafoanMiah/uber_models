import streamlit as st
import pandas as pd
import numpy as np
import pickle
from geopy.geocoders import Nominatim
from datetime import datetime

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')))
import distance_utils


#title / description
st.markdown("<h1 style='text-align: center;'> Price Prediction Model </h1>", unsafe_allow_html=True)
st.markdown('---')



pickup_address = 'London'  #london
dropoff_address = 'California' #california


#using adress
loc = Nominatim(user_agent="Geopy Library")

col1, col2= st.columns(2)
with col1:
    pickup_address = st.text_input('Pickup Address', value='London')
    
with col2:
    dropoff_address = st.text_input('Dropoff Address', value='California')

st.markdown("<p style='text-align: center;'> OR </p>", unsafe_allow_html=True)






getPLoc = loc.geocode(pickup_address)
pickup_lat, pickup_long = getPLoc.latitude, getPLoc.longitude

col1_1, col1_2= st.columns(2)
with col1_1:
    pickup_lat = st.number_input('Pickup Latitude', value=pickup_lat)
with col1_2:
    pickup_long = st.number_input('Pickup Longitude', value=pickup_long)


getDLoc = loc.geocode(dropoff_address)
dropoff_lat, dropoff_long = getDLoc.latitude, getDLoc.longitude

col1_1, col1_2= st.columns(2)
with col1_1:
    pickup_lat = st.number_input('Dropoff Latitude', value=pickup_lat)
with col1_2:
    pickup_long = st.number_input('Dropoff Longitude', value=pickup_long)


st.markdown("<p style='text-align: center;'> OPTIONAL </p>", unsafe_allow_html=True)
#other inputs
col1, col2= st.columns(2)
with col1:
    current_year = datetime.now().year
    print(current_year)
    year = st.selectbox('Year', (range(2010, current_year+1)), index=len(range(2010, current_year+1))-1)
with col2:
    month = st.selectbox('Month', (range(1, 13)))

col1, col2= st.columns(2)
with col1:
    day = st.selectbox('Day', (range(1, 8)))
with col2:
    hour = st.selectbox('Hour', (range(0, 24)))



#mapping
locations = pd.DataFrame({
    'type': ['green', 'red'],
    'lat' : [float(pickup_lat), float(dropoff_lat)],
    'long': [float(pickup_long), float(dropoff_long)]
})

st.map(locations, latitude='lat', longitude='long', size=10, color='#a6f1a6')
st.markdown('---')




#model_path = 'uber_cost_prediction/model/trained_model.pkl'
#with open(model_path, 'rb') as f:
#    model = pickle.load(f)

distance = distance_utils.haversine(pickup_long, pickup_lat, dropoff_long, dropoff_lat)

st.markdown("<h3 style='text-align: center;'>Daframe:</h3>", unsafe_allow_html=True)
features = pd.DataFrame({
    'distance_km': [distance],
    'pickup_longitude': [pickup_long],
    'pickup_latitude': [pickup_lat],
    'dropoff_longitude': [dropoff_long],
    'dropoff_latitude': [dropoff_lat],
    'passenger_count': [1],
    'year': [year],
    'month': [month],
    'day': [day],
    'hour': [hour]
})

st.dataframe(features)
