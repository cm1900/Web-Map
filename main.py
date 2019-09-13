import folium
map = folium.Map(location =[-10, 28], zoom_start = 3, tiles = "Stamen Terrain")
map.save("map1.html")