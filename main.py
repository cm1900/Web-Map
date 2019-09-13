import folium
map = folium.Map(location =[-10, 28], zoom_start = 3, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location =[-3, 28], popup ="Danger Zone", icon =folium.Icon(color='red')))
map.add_child(fg)
map.save("map1.html")