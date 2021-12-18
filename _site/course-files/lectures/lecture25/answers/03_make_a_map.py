# pip3 install folium
# or
# pip install folium
import folium
import utilities
from csv import reader

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

for row in rows[1:200]: 
    lat_lng = row[0]
    lat_lng = lat_lng.split('(')[1]
    lng = float(lat_lng.split(' ')[0])
    lat = lat_lng.split(' ')[1]
    lat = float(lat.replace(')', ''))
    common_name = row[39].replace('"', '').lower()
    #print(lat, lng)
    marker = folium.Marker(
        location=[lat, lng],
        popup=common_name
    )
    marker.add_to(map)


# for business in businesses:
#     # print(business)
#     lat = business.get('coordinates').get('latitude')
#     lng = business.get('coordinates').get('longitude')
#     if lat and lng:
#         # print(lat, lng)
#         marker = folium.Marker(
#             location=[lat, lng],
#             popup=business.get('name')
#         )
#         marker.add_to(map)


# # show map:
map.save(utilities.get_file_path('my_map.html', subdirectory='results'))