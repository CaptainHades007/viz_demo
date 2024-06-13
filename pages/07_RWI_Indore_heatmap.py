import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from streamlit_folium import folium_static
from datasets import names
@st.cache_data
def load_data_1():
    data = pd.read_csv(names.RWI_INDORE_DATA_1)
    return data

# Load data
data = load_data_1()

m1=folium.Map(location=[data.latitude.mean(),data.longitude.mean()],zoom_start=8,control_scale=True)
m1.fit_bounds([[21, 74], [24, 77]])
map_values = data[['latitude','longitude','label']]
dat = map_values.values.tolist()
hm = HeatMap(dat,min_opacity=0.2,max_opacity=0.8,radius = 20).add_to(m1)
# st_folium(m1)
folium_static(m1)
