import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
from datasets import names

# Function to load data
@st.cache_data
def load_data():
    data = pd.read_csv(names.INDORE_DATA_1)
    return data

# Load data
data = load_data()
data['class'] = data['label'].map({0: 'BPL', 1: 'APL'})
# Streamlit webpage title
st.title('Indore prediction')

# Sidebar for user input features
# st.sidebar.header('Filters')

fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_data=["latitude", "longitude", "class"],
                        zoom=10, height=600)

# Set marker color based on label
fig.update_traces(marker=dict(color=data['class'].map({'BPL': 'blue', 'APL': 'red'}),size=8))

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the plot
# fig.show()# Plot similar songs
st.plotly_chart(fig)


m1=folium.Map(location=[data.latitude.mean(),data.longitude.mean()],zoom_start=8,control_scale=True)
# m1.fit_bounds([[27, 74], [31, 79]])
map_values = data[['latitude','longitude','label']]
dat = map_values.values.tolist()
hm = HeatMap(dat,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'blue', 0.5: 'lime', 1.0: 'red'},radius = 20).add_to(m1)
# st_folium(m1)



# st_folium(m1, use_container_width=True)
folium_static(m1, width=650, height=650)
st.write('Predicted Heatmap')

# Run this with `streamlit run your_script_name.py`
# Run this with `streamlit run your_script_name.py`
