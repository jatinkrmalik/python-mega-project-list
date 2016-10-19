# Fetch Current Weather 
# Get the current weather for a given zip/postal code. Optional: Try locating the user automatically

import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

print("Fetching location...")
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = str(j['latitude'])
lon = str(j['longitude'])
print("Getting weather for Latitude:",lat,"and Longitude",lon,"...")

wPage = urlopen("https://weather.com/en-IN/weather/today/l/"+lat+","+lon)

soup = bs(wPage, "html5lib")

print(soup.prettify())
