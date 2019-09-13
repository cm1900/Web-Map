import folium
import pandas

data = pandas.read_csv("data/volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
loc = list(data['LOCATION'])
elev = list(data['ELEV'])

def get_color(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location =[8, 10], zoom_start = 2,
tiles = "Stamen Terrain")
fgVolcanoes = folium.FeatureGroup(name="North America Volcanoes")
fgPopulation = folium.FeatureGroup(name="Populations")

for lt, ln, nm, lc, elv in zip(lat, lon, name, loc, elev):
    pos = [lt, ln]
    msg = "Name: {}\nLocation: {}\nElevation: {} ".format(nm, lc, elv)
    fgVolcanoes.add_child(folium.CircleMarker(location =pos, popup =msg, 
    fill_color=get_color(elv), color='gray', fill_opacity = 0.7, radius = 6))

fgPopulation.add_child(folium.GeoJson(data =open('data/world.json', 'r', 
encoding = 'utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000
else 'blue' if 20000000 <= x['properties']['POP2005']<50000000
else 'red'}))

map.add_child(fgVolcanoes)
map.add_child(fgPopulation)
map.add_child(folium.LayerControl())
map.save("map1.html")