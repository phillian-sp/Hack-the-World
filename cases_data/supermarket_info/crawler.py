from urllib.request import urlopen, Request
import csv
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import sys
geolocator = Nominatim(user_agent="hacktheworld")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}#{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

reg_url = "http://supermarketpage.com/state/CA/"
req = Request(url=reg_url, headers=headers) 
response = urlopen(req).read() 

# response = urllib.request.urlopen('http://supermarketpage.com/state/CA/')

#print(response.status)
soup = BeautifulSoup(response, features="lxml")
table = soup.table
table_row = table.find_all("tr")

with open("/Users/phillipmiao/WorkSpaces/Hack-the-World/cases_data/supermarket_info/supermarket.csv", 'w') as f:
    csvwriter = csv.writer(f)
    urls = []
    for row in table_row:
        data = {}
        cols = row.find_all("td")
        if cols[0].text == "Name":
            continue
        data['name'] = cols[0].text
        data['url'] = cols[0].a['href']
        urls.append(data)
        
        # csvwriter.writerow(data)
    
    csvwriter.writerow(["Name", "Address", "Zip Code", "Phone #"])
    null_counter = 0
    for url in urls:
        req = Request(url=url['url'], headers=headers) 
        response = urlopen(req).read()
        soup = BeautifulSoup(response, features="lxml")
        table = soup.table
        table_row = table.find_all("tr")
        print(url['name'])
        count = 0
        found = False
        for row in table_row:
            data = []
            cols = row.find_all("td")
            if cols[2].text != "CA":
                if found:
                    print("break")
                    break
                else:
                    continue
            found = True
            address = cols[1].text[1:-2]
            location = geolocator.geocode(address + " " + cols[3].text)
            if location is None:
                null_counter += 1
                print(f"*** skipped {null_counter}")
                continue
            csvwriter.writerow([url['name'], address, location.latitude, location.longitude, cols[3].text, cols[4].text])

            count += 1
            print(f"    done {count} out of {len(table_row) - 1}")
            

    
