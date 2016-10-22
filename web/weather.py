# Fetch Current Weather 
# Get the current weather for a given zip/postal code. Optional: Try locating the user automatically

import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from geopy.geocoders import Nominatim # 'pip3 install geopy' to install geopy

def getLocAuto():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = str(j['latitude'])
    lon = str(j['longitude'])
    city = str(j['city'])
    return lat,lon,city

def getLocByPin(pincode):
    geolocator = Nominatim()
    location = geolocator.geocode(pincode)
    lat = str(location.latitude)
    lon = str(location.longitude)
    address = location.address
    return lat,lon,address

def getWeather(lat,lon):
    wPage = urlopen("https://darksky.net/"+lat+","+lon)
    soup = bs(wPage, "html5lib")
    temp = soup.select("body.forecast #title span.temp")[0].get_text()[:2:]
    summary = soup.select("body.forecast #title span.summary")[0].get_text()
    msg = soup.select("body.forecast #title .next.swap")[0].get_text()
    return temp, summary, msg

print("\n\t\tWeather Channel!\n")
ch = input("Get me weather for:\n(C)urrent location\n(P)in code\n\n>>Enter your choice: ").lower()

if ch == 'c':
    print("\nFetching location...")
    lat, lon, city = getLocAuto()
    print("\nGetting weather for",city," -  Latitude:",lat,"and Longitude",lon,"...")
    temp, summary, msg = getWeather(lat, lon)
    print()
    print("#"*50)
    print("\n>>>Weather at",city,"<<<\n",temp,"degree celcius\n",summary,msg)
    print("#"*50)

elif ch == 'p':
    pincode = input("Enter the pin code :")
    lat,lon,address = getLocByPin(pincode)
    print("Getting weather for",address," -  Latitude:",lat,"and Longitude",lon,"...")
    temp, summary, msg = getWeather(lat, lon)
    print()
    print("#"*50)
    print("\n>>>Weather at",address,"<<<\n",temp,"degree celcius\n",summary,msg)
    print("#"*50)
