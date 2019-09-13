import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])

map = folium.Map(location =[38.58, -99.09], zoom_start = 4, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(location =[lt, ln], popup =nm, icon =folium.Icon(color='red')))

map.add_child(fg)
map.save("map1.html")