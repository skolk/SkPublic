import folium

map = folium.Map(location =[42.363868, -71.095041], zoom_start=10, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[42.363868, -71.095041]))# popup="Hi I'm a marker"))# icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map123.html")
