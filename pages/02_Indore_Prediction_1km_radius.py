import streamlit as st
import pandas as pd
import plotly.express as px

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
fig.update_traces(marker=dict(color=data['class'].map({'BPL': 'yellow', 'APL': 'red'}),size=8))

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the plot
# fig.show()# Plot similar songs
st.plotly_chart(fig)

# Run this with `streamlit run your_script_name.py`