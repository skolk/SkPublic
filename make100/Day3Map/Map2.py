import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
vona = list(data["NAME"])
elev = list(data["ELEV"])


def colorPicker(x):
    if x < 2000:
        return 'green'
    elif x > 3000:
        return 'red'

map = folium.Map(location =[46.7859564,-123.5415815], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes_USA")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, vn, el in zip(lat, lon, vona, elev):
    x = str(vn) + ", " + str(el) + "m"
    fgv.add_child(folium.CircleMarker(
            location=[lt, ln],
            radius= 6,
            color=colorPicker(el),
            fill=True,
            fill_color=colorPicker(el),
            fill_opacity=.5,
            popup=folium.Popup(str(x),parse_html=True)))

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'red'if x['properties']['POP2005'] <10000000
else 'blue' if x['properties']['POP2005'] <20000000
else 'green' if x['properties']['POP2005'] <30000000 else'grey'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map2.html")
