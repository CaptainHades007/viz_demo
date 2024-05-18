import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
from datasets import names
st.set_page_config(layout="wide")
# Function to load data
@st.cache_data
def load_data_1():
    data = pd.read_csv(names.HARYANA_DATA_1)
    return data
def load_data_2():
    data = pd.read_csv(names.HARYANA_DATA_2)
    return data

# Load data
data = load_data_1()
data2 = load_data_2()

data['class'] = data['label'].map({0: 'BPL', 1: 'APL'})
data2['class'] = data2['label'].map({0: 'BPL', 1: 'APL'})

# Streamlit webpage title
st.title('Haryana model comparison heatmap')



m1=folium.Map(location=[data.latitude.mean(),data.longitude.mean()],zoom_start=8,control_scale=True)
m1.fit_bounds([[27, 74], [31, 79]])
map_values = data[['latitude','longitude','label']]
dat = map_values.values.tolist()
hm = HeatMap(dat,min_opacity=0.2,max_opacity=0.8,radius = 20).add_to(m1)
# st_folium(m1)

m2=folium.Map(location=[data2.latitude.mean(),data2.longitude.mean()],zoom_start=8,control_scale=True)
m2.fit_bounds([[27, 74], [31, 79]])
map_values = data2[['latitude','longitude','label']]
dat2 = map_values.values.tolist()
hm2 = HeatMap(dat2,min_opacity=0.2,max_opacity=0.8,radius = 20).add_to(m2)
# st_folium(m2)

col3, col4 = st.columns(2)

with col3:
    # st_folium(m1, use_container_width=True)
    folium_static(m1, width=650, height=650)
    st.write('Predicted Heatmap')

with col4:
    # st_folium(m2, use_container_width=True)
    folium_static(m2, width=650, height=650)
    st.write("Actual Heatmap")
# Run this with `streamlit run your_script_name.py`
