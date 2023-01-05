import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium import plugins
from scipy import stats




def create_heatmap(df):
    y = df[['GEO_LAT', 'GEO_LON']][(df['GEO_LAT'] > 38) & (df['GEO_LAT'] < 41)]
    y.dropna(inplace=True)

    denver_crime_heatmap = folium.Map()
    denver_crime_heatmap.add_child(plugins.HeatMap(data=y, min_opacity=0.55, radius=16))
    return denver_crime_heatmap

