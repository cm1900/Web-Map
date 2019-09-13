import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
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

map = folium.Map(location =[38.58, -99.09], zoom_start = 4, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm, lc, elv in zip(lat, lon, name, loc, elev):
    pos = [lt, ln]
    msg = "Name: {}\nLocation: {}\nElevation: {} ".format(nm, lc, elv)
    fg.add_child(folium.Marker(location =pos, popup =msg, icon =folium.Icon(color=get_color(elv))))

map.add_child(fg)
map.save("map1.html")