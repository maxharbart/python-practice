import folium
import pandas

data = pandas.read_csv('Volcanoes.csv')
latitude = list(data['LAT'])
longitude = list(data['LON'])
name = list(data['NAME'])
elev = list(data['ELEV'])


m = folium.Map(location=[45.5236, -122.6750])

def elev_color(x):
    if x > 3000:
        return 'red'   
    elif x < 3000 and x > 2000:
        return 'orange'
    elif x < 2000 and x > 2000:
        return 'yellow'
    else:
        return 'green'


for i in range(0, len(data.index)):
    folium.Marker(
        location=[latitude[i], longitude[i]],
        popup=name[i] + ' ' + str(elev[i]) + ' meters',
        icon=folium.Icon(icon='fire', color=elev_color(elev[i]))
        ).add_to(m)


m.save('map.html')