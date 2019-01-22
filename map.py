import folium

# I can create a map object as such:
map = folium.Map(location=[40.735179, -73.988025], zoom_start=5, tiles="Mapbox Bright")

# I can add individual child objects on my map object
map.add_child(folium.Marker(location=[40.735179, -73.988025], popup="Shawn Your Here"))

# another way to pass objects to a map is a feature group which is more like component based
fg = folium.FeatureGroup(name="map1")
# to add a specific component
fg.add_child(folium.Marker(location=[40.748440, -73.985664], popup="Empire State building"))
fg.add_child(folium.Marker(location=[40.713005, -74.013184], popup="One World Trade"))

# add components to the map as one child
map.add_child(fg)

map.save("firstMap.html")
