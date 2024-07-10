import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

import os, sys
sys.path.append(os.path.join(os.getcwd(), '..', 'scripts'))
import distance_utils


#title / description
st.markdown("<h2 style='text-align: center;'> Price Prediction Model </h2>", unsafe_allow_html=True)

st.markdown('---')



pickup_address, pickup_lat, pickup_long = None, 0.1276, 51.5072,  #london
dropoff_address, dropoff_lat, dropoff_long = None, 119.4179, 36.7783 #california


#using adress
loc = Nominatim(user_agent="Geopy Library")

col1, col2= st.columns(2)
with col1:
    pickup_address = st.text_input('Pickup Address')
    
with col2:
    dropoff_address = st.text_input('Dropoff Address')

st.markdown("<p style='text-align: center;'> OR </p>", unsafe_allow_html=True)





#with latitude and longitude
if pickup_address:
    getPLoc = loc.geocode(pickup_address)
    pickup_lat, pickup_long = getPLoc.latitude, getPLoc.longitude
    
    col1_1, col1_2= st.columns(2)
    with col1_1:
        pickup_lat = st.number_input('Pickup Latitude', value=pickup_lat)
    with col1_2:
        pickup_long = st.number_input('Pickup Longitude', value=pickup_long)
else:
    #using lat long
    col1_1, col1_2= st.columns(2)
    with col1_1:
        pickup_lat = st.number_input('Pickup Latitude')
    with col1_2:
        pickup_long = st.number_input('Pickup Longitude')


if dropoff_address:
    getDLoc = loc.geocode(dropoff_address)
    dropoff_lat, dropoff_long = getDLoc.latitude, getDLoc.longitude
    
    col1_1, col1_2= st.columns(2)
    with col1_1:
        pickup_lat = st.number_input('Dropoff Latitude', value=pickup_lat)
    with col1_2:
        pickup_long = st.number_input('Dropoff Longitude', value=pickup_long)
else:
    col2_1, col2_2= st.columns(2)
    with col2_1:
        dropoff_lat = st.number_input('Dropoff Latitude')
    with col2_2:
        dropoff_long = st.number_input('Dropoff Longitude')




#mapping
locations = pd.DataFrame({
    'type': ['green', 'red'],
    'lat' : [float(pickup_lat), float(dropoff_lat)],
    'long': [float(pickup_long), float(dropoff_long)]
})

st.map(locations, latitude='lat', longitude='long', size=5, color='#a6f1a6')
