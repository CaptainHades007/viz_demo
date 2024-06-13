import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from streamlit_folium import folium_static
from branca.element import Template, MacroElement
from datasets import names
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

<div class='legend-title'>Legend</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:red;opacity:0.7;'></span>High RWI</li>
    <li><span style='background:blue;opacity:0.7;'></span>Low RWI</li>

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

@st.cache_data
def load_data_1():
    data = pd.read_csv(names.RWI_HARYANA_DATA_1)
    return data

# Load data
data = load_data_1()

m1=folium.Map(location=[data.latitude.mean(),data.longitude.mean()],zoom_start=8,control_scale=True)
m1.fit_bounds([[27, 74], [31, 79]])
map_values = data[['latitude','longitude','rwi']]
dat = map_values.values.tolist()
hm = HeatMap(dat,min_opacity=0.2,max_opacity=0.8,radius = 20).add_to(m1)
m1.add_child(macro)
# st_folium(m1)
folium_static(m1)
