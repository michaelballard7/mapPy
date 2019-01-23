import folium
import pandas as pd, io  

# I can create a map object as such:
map = folium.Map(location=[40.735179, -73.988025], zoom_start=5, tiles="Mapbox Bright")

# I can add individual child objects on my map object
map.add_child(folium.Marker(location=[40.735179, -73.988025], popup="Shawn Your Here"))

# another way to pass objects to a map is a feature group which is more like component based
fg = folium.FeatureGroup(name="map1")
# to add a specific component
fg.add_child(folium.Marker(location=[40.748440, -73.985664], popup="Empire State building"))
fg.add_child(folium.Marker(location=[40.713005, -74.013184], popup="One World Trade"))

# import pandas volcanoe data and prepare to add to the map
data = pd.read_csv("../data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# a function to determine the color of a map marker:
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# add multiple children from a structured pandas dataset
for lt, ln, el in zip(lat, lon, elev):
    # add a child using circle markers pads
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"Meter", fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.save("map2.html")
