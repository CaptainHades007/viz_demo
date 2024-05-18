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

data_0 = data[data['label']==0]
data_1 = data[data['label']==1]
data2_0 = data2[data2['label']==0]
data2_1 = data2[data2['label']==1]


m3=folium.Map(location=[data_1.latitude.mean(),data_1.longitude.mean()],zoom_start=8,control_scale=True)
# m1.fit_bounds([[27, 74], [31, 79]])
map_values1 = data_1[['latitude','longitude','label']]
map_values0 = data_0[['latitude','longitude','label']]
dat1 = map_values1.values.tolist()
dat0 = map_values0.values.tolist()
hm3 = HeatMap(dat1,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'white',  1.0: 'red'},radius = 25).add_to(m3)
hm4 = HeatMap(dat0,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'cyan',  1.0: 'white'},radius = 25).add_to(m3)
# folium_static(m3, width=650, height=650)
# st.write("Predicted Heatmap for combined localities")

m4=folium.Map(location=[data2_1.latitude.mean(),data2_1.longitude.mean()],zoom_start=8,control_scale=True)
# m1.fit_bounds([[27, 74], [31, 79]])
map_values1 = data2_1[['latitude','longitude','label']]
map_values0 = data2_0[['latitude','longitude','label']]
dat1 = map_values1.values.tolist()
dat0 = map_values0.values.tolist()
hm3 = HeatMap(dat1,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'white',  1.0: 'red'},radius = 25).add_to(m4)
hm4 = HeatMap(dat0,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'cyan',  1.0: 'white'},radius = 25).add_to(m4)
# folium_static(m4, width=650, height=650)
# st.write("actual Heatmap 2 for combined localities")

col5, col6 = st.columns(2)

with col5:
    # st_folium(m1, use_container_width=True)
    folium_static(m3, width=650, height=650)
    st.write('Predicted Heatmap')

with col6:
    # st_folium(m2, use_container_width=True)
    folium_static(m4, width=650, height=650)
    st.write("Actual Heatmap")
