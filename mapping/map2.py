import folium
import pandas

data = pandas.read_csv('Volcanoes.csv')
latitude = list(data['LAT'])
longitude = list(data['LON'])
name = list(data['NAME'])


m = folium.Map(location=[45.5236, -122.6750])



for i in range(0, len(data.index)):
    folium.Marker(
        location=[latitude[i], longitude[i]],
        popup=name[i],
        icon=folium.Icon(icon='fire')
        ).add_to(m)


m.save('map.html')