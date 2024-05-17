import streamlit as st
import pandas as pd
import plotly.express as px

from datasets import names

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
fig1 = go.Figure(go.Scattermapbox(
    lat=data['latitude'],
    lon=data['longitude'],
    mode='markers',
    marker=dict(color=data['label'].map({0: 'yellow', 1: 'red'})),
    text=data[['latitude', 'longitude', 'label']],
    name='Data 1'
))

# Set layout for the first plot
fig1.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=data['latitude'].mean(), lon=data['longitude'].mean()),
        zoom=10
    ),
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Create the second scatter plot for data2
fig2 = go.Figure(go.Scattermapbox(
    lat=data2['latitude'],
    lon=data2['longitude'],
    mode='markers',
    marker=dict(color=data2['label'].map({0: 'yellow', 1: 'red'})),
    text=data2[['latitude', 'longitude', 'label']],
    name='Data 2'
))

# Set layout for the second plot
fig2.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=data2['latitude'].mean(), lon=data2['longitude'].mean()),
        zoom=10
    ),
    margin={"r":0,"t":0,"l":0,"b":0}
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
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)
# Run this with `streamlit run your_script_name.py`
