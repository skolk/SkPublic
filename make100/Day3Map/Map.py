import folium

map = folium.Map(location =[42.363868, -71.095041], zoom_start=10, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker([45.3288, -121.6625],
              popup='Mt. Hood Meadows',
              icon=folium.Icon(icon='cloud')))
map.add_child(fg)

map.save("Map123.html")
