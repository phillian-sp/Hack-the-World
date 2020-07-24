from urllib.request import urlopen, Request
import csv
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="hacktheworld")


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}#{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

reg_url = "https://ccfoodbank.org/food-locator/"
req = Request(url=reg_url, headers=headers) 
response = urlopen(req).read() 

soup = BeautifulSoup(response, features="lxml")
divs = soup.find(id="storeLocator__storeList").find_all("div")
f = open("./food_center_info/a.txt", 'w')
f.write(str(soup))
with open("./food_center_info/supermarket.csv", 'w') as f:
    csvwriter = csv.writer(f)

    csvwriter.writerow(["Name", "Address" , "Phone #","Open Time"])
    for div in divs:

        name = row.find({"name":"store-location"}).text
        address = row.find({"name":"store-address"}).text
        location = geolocator.geocode(address)
        tel = row.find({"name":"store-tel"}).text
        time = row.find({"name":"store-description"}).text
        print(name)
        
        csvwriter.writerow([name,address,location.latitude,location.longitude,tel, time])