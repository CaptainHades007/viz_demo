import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
from datasets import names
from branca.element import Template, MacroElement

# ...

HeatMap(heat_data, radius=15).add_to(france_map)

# Custom draggable legend in HTML & CSS
template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>


<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>

<div class='legend-title'>Legend (draggable!)</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:red;opacity:0.7;'></span>Big</li>
    <li><span style='background:orange;opacity:0.7;'></span>Medium</li>
    <li><span style='background:green;opacity:0.7;'></span>Small</li>

  </ul>
</div>
</div>

</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

# Add MacroElement to HeatMap
macro = MacroElement()
macro._template = Template(template)
# france_map.add_child(macro)
# france_map.save('urban_trees_density_map.html')

# Function to load data
@st.cache_data
def load_data():
    data = pd.read_csv(names.INDORE_DATA_2)
    return data

# Load data
data = load_data()
data['class'] = data['label'].map({0: 'BPL', 1: 'APL'})
data_0 = data[data['label'] == 0]
data_1 = data[data['label'] == 1]
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


m1=folium.Map(location=[data_0.latitude.mean(),data_0.longitude.mean()],zoom_start=8,control_scale=True)
# m1.fit_bounds([[27, 74], [31, 79]])
map_values = data_0[['latitude','longitude','label']]
dat = map_values.values.tolist()
hm2 = HeatMap(dat,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'cyan',  1.0: 'white'},radius = 25).add_to(m1)
# st_folium(m1)

# ,gradient={0.0: 'lightblue',  1.0: 'red'}

# st_folium(m1, use_container_width=True)
m1.add_child(macro)
folium_static(m1, width=650, height=650)
st.write('Predicted Heatmap for poor localities')

m2=folium.Map(location=[data_1.latitude.mean(),data_1.longitude.mean()],zoom_start=8,control_scale=True)
# m1.fit_bounds([[27, 74], [31, 79]])
map_values = data_1[['latitude','longitude','label']]
dat = map_values.values.tolist()
hm = HeatMap(dat,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'white',  1.0: 'red'},radius = 25).add_to(m2)
# st_folium(m1)

# ,gradient={0.0: 'lightblue',  1.0: 'red'}

# st_folium(m1, use_container_width=True)
folium_static(m2, width=650, height=650)
st.write('Predicted Heatmap for rich localities')
# col3, col4 = st.columns(2)

# with col3:
#     # st_folium(m1, use_container_width=True)
#     folium_static(m1, width=550, height=650)
#     st.write('Predicted Heatmap for poor localities')

# with col4:
#     # st_folium(m2, use_container_width=True)
#     folium_static(m2, width=550, height=650)
#     st.write("Predicted Heatmap for rich localities")

m3=folium.Map(location=[data_1.latitude.mean(),data_1.longitude.mean()],zoom_start=8,control_scale=True)
# m1.fit_bounds([[27, 74], [31, 79]])
map_values1 = data_1[['latitude','longitude','label']]
map_values0 = data_0[['latitude','longitude','label']]
dat1 = map_values1.values.tolist()
dat0 = map_values0.values.tolist()
hm3 = HeatMap(dat1,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'white',  1.0: 'red'},radius = 25).add_to(m3)
hm4 = HeatMap(dat0,min_opacity=0.2,max_opacity=0.8,gradient={0.0: 'cyan',  1.0: 'white'},radius = 25).add_to(m3)
folium_static(m3, width=650, height=650)
st.write("Predicted Heatmap for combined localities")
# Run this with `streamlit run your_script_name.py`
# Run this with `streamlit run your_script_name.py`
