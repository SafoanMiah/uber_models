import streamlit as st
from geopy.geocoders import Nominatim

import os, sys
sys.path.append(os.path.join(os.getcwd(), '..', 'scripts'))
import distance_utils


#title / description
st.markdown("<h2 style='text-align: center;'> Price Prediction Model </h2>", unsafe_allow_html=True)

st.markdown('---')



pickup_address, pickup_lat, pickup_long = None, None, None
dropoff_address, dropoff_lat, dropoff_long = None, None, None


#using adress
loc = Nominatim(user_agent="Geopy Library")

col1, col2= st.columns(2)
with col1:
    pickup_address = st.text_input('Pickup Address')
    
with col2:
    dropoff_address = st.text_input('Dropoff Address')

st.markdown("<p style='text-align: center;'> OR </p>", unsafe_allow_html=True)






if pickup_address:
    getPLoc = loc.geocode(pickup_address)
    pickup_lat, pickup_long = getPLoc.latitude, getPLoc.longitude
    
    col1_1, col1_2= st.columns(2)
    with col1_1:
        pickup_lat = st.text_input('Pickup Latitude', value=pickup_lat)
    with col1_2:
        pickup_long = st.text_input('Pickup Longitude', value=pickup_long)
else:
    #using lat long
    col1_1, col1_2= st.columns(2)
    with col1_1:
        pickup_lat = st.text_input('Pickup Latitude')
    with col1_2:
        pickup_long = st.text_input('Pickup Longitude')


if dropoff_address:
    getDLoc = loc.geocode(dropoff_address)
    dropoff_lat, dropoff_long = getDLoc.latitude, getDLoc.longitude
    
    col1_1, col1_2= st.columns(2)
    with col1_1:
        pickup_lat = st.text_input('Dropoff Latitude', value=pickup_lat)
    with col1_2:
        pickup_long = st.text_input('Dropoff Longitude', value=pickup_long)
else:
    col2_1, col2_2= st.columns(2)
    with col2_1:
        dropoff_lat = st.text_input('Dropoff Latitude')
    with col2_2:
        dropoff_long = st.text_input('Dropoff Longitude')