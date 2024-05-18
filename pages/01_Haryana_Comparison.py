import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
st.title('Haryana model comparison')

# # Sidebar for user input features
# # st.sidebar.header('Filters')

# fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_data=["latitude", "longitude", "label"],
#                         zoom=10, height=600)

# # Set marker color based on label
# fig.update_traces(marker=dict(color=data['label'].map({0: 'yellow', 1: 'red'})))

# fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# # Show the plot
# # fig.show()# Plot similar songs
# st.plotly_chart(fig)
# Create the first scatter plot for data
# fig1 = go.Figure(go.Scattermapbox(
#     lat=data['latitude'],
#     lon=data['longitude'],
#     mode='markers',
#     marker=dict(color=data['label'].map({0: 'yellow', 1: 'red'})),
#     text=data[['latitude', 'longitude', 'label']],
#     name='Data 1'
# ))

# # Set layout for the first plot
# fig1.update_layout(
#     mapbox=dict(
#         style="open-street-map",
#         center=dict(lat=data['latitude'].mean(), lon=data['longitude'].mean()),
#         zoom=10
#     ),
#     margin={"r":0,"t":0,"l":0,"b":0}
# )

# # Create the second scatter plot for data2
# fig2 = go.Figure(go.Scattermapbox(
#     lat=data2['latitude'],
#     lon=data2['longitude'],
#     mode='markers',
#     marker=dict(color=data2['label'].map({0: 'yellow', 1: 'red'})),
#     text=data2[['latitude', 'longitude', 'label']],
#     name='Data 2'
# ))

# # Set layout for the second plot
# fig2.update_layout(
#     mapbox=dict(
#         style="open-street-map",
#         center=dict(lat=data2['latitude'].mean(), lon=data2['longitude'].mean()),
#         zoom=10
#     ),
#     margin={"r":0,"t":0,"l":0,"b":0}
# )


fig1 = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_data=["latitude", "longitude", "class"],
                        zoom=7, height=600, width=600)

# Set marker color based on label
fig1.update_traces(marker=dict(color=data['class'].map({'BPL': 'blue', 'APL': 'red'}),size=7))
# inimum Latitude: 27.93° N
# Maximum Latitude: 30.33° N
# Minimum Longitude: 74.43° E
# Maximum Longitude: 77.59° E
fig1.update_layout(mapbox_style="open-street-map")
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig1.update_layout(
    mapbox=dict(
        center=dict(lat=29, lon=76),
        # Set the range of latitude and longitude for the window
        # Replace the values with your desired range
        # bounds=dict(x=[74, 78], y=[27, 31]),
        bounds=dict(west=74,
            east=79,
            south=27,
            north=31),
        zoom=7
    )
)

# Create the second scatter plot for data2
fig2 = px.scatter_mapbox(data2, lat="latitude", lon="longitude", hover_data=["latitude", "longitude", "class"],
                        zoom=7, height=600, width=600)

# Set marker color based on label
fig2.update_traces(marker=dict(color=data2['class'].map({'BPL': 'blue', 'APL': 'red'}),size=7))

fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig2.update_layout(
    mapbox=dict(
        center=dict(lat=29, lon=76),
        # Set the range of latitude and longitude for the window
        # Replace the values with your desired range
        # bounds=dict(x=[74, 78], y=[27, 31]),
        bounds=dict(west=74,
            east=79,
            south=27,
            north=31),
        zoom=7
    )
)
# Display the plots using Streamlit
# Display the plots using Streamlit
# st.write("# Data 1")
# st.plotly_chart(fig1)

# st.write("# Data 2")
# st.plotly_chart(fig2)
# Display figures side by side
# Display figures side by side
col1, col2 = st.columns(2)

with col1:
    st.write('Predicted Classification')
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.write('Actual Classification')
    st.plotly_chart(fig2, use_container_width=True)

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
