import folium

map = folium.Map(location=[34.130923, -118.041751], 
                 tiles="Stamen Toner",
                zoom_start=5)
with open("/Users/phillipmiao/WorkSpaces/Hack-the-World/cases_data/supermarket_info/supermarket.csv", 'w') as f:
    datas = csv.DictReader(f)
    for data in datas:
        print(f"<strong>H Mart</strong><br>{data['Name']}<br>{data['Address']}<br>{data["Phone #"]}<br>Supplies:<br><ul><li>Masks</li><li>Fish</li></ul>")
        folium.Marker(location=[data["Lat"],data["Lon"]],
              popup=(f"<strong>H Mart</strong><br>{data['Name']}<br>{data['Address']}<br>{data["Phone #"]}<br>Supplies:<br><ul><li>Masks</li><li>Fish</li></ul>"), 
              tooltip=data['Name'],
              icon=folium.Icon(color="red", icon='shopping-cart', prefix='fa')).add_to(map)
map.save('index.html')