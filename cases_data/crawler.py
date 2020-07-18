import urllib.request
import csv
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://publichealth.lacounty.gov/media/coronavirus/locations.htm')
print(response.status)
soup = BeautifulSoup(response, features="lxml")
table = soup.table
table_row = table.find_all("tr")

with open("cases.csv", 'w') as f:
    csvwriter = csv.writer(f)
    start = False
    for row in table_row:
        data = []
        cols = row.find_all("td")
        if cols[0].text == "CITY/COMMUNITY**":
            start = True
        
        if not start:
            continue
        
        for col in cols:
            data.append(col.text)
        
        csvwriter.writerow(data)