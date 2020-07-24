import folium
import csv
import geopy
geopy.geocoders.options.default_timeout = 10000
geolocator = geopy.geocoders.Nominatim(user_agent="hacktheworld")

map = folium.Map(location=[34.130923, -118.041751], 
                 tiles="Stamen Toner",
                zoom_start=13)

# with open("/Users/phillipmiao/WorkSpaces/Hack-the-World/cases_data/supermarket_info/supermarket.csv", 'r') as f:
#     datas = csv.DictReader(f)
#     null_counter = 0
#     for data in datas:
#         print(data)
#         # try:
#         location = geolocator.geocode(data['Address'] + ", CA " + data['Zip Code'])
#         # except socket.timeout:
#             # geolocator = Nominatim(user_agent="hacktheworld")
#             # location = geolocator.geocode(data['Address'] + ", CA " + data['Zip Code'])
#         if location is None:
#             null_counter += 1
#             print(f"*** skipped {null_counter}")
#             # if(null_counter > 1): break
#             continue
#         folium.Marker(location=[location.latitude,location.longitude],
#               popup=folium.Popup(f"<strong>{data['Name']}</strong><br>{data['Address']}<br>{data['Phone #']}<br>Supplies:<br><ul><li>Masks</li><li>Fish</li></ul>",max_width=2650),
#               tooltip=data['Name'],
#               icon=folium.Icon(color="red", icon='shopping-cart', prefix='fa')).add_to(map)

map.save("/Users/phillipmiao/WorkSpaces/Hack-the-World/Website_for_hackathon/map/map.html⁩")