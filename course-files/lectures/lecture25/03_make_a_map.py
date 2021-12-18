# pip3 install folium
# or
# pip install folium
import folium
import utilities
from csv import reader

# open the file and save all the records to a variable called "rows"
file_path = utilities.get_file_path('Trees_data.csv')
f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f)) # save all the rows as a list


# create map centered at first business retrieved:
center_lng = -87.683211115658
center_lat = 42.062932975533
map = folium.Map(
    location=[center_lat, center_lng],  #lat, lng
    zoom_start=13,
    tiles="Stamen watercolor"
)

# code to create a marker:
marker = folium.Marker(
    location=[center_lat, center_lng],
    popup='Evanston'
)
marker.add_to(map)

map.save(utilities.get_file_path('my_map.html', subdirectory='results'))