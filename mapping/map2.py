import folium

m = folium.Map(location=[45.5236, -122.6750])
folium.Marker(
    location=[45.3288, -121.6625],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

m.save('map.html')