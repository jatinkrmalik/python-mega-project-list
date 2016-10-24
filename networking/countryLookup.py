# Country from IP Lookup
# Enter an IP address and find the country that IP is registered in. Optional: Find the Ip automatically.

import requests
import json
from time import sleep
import os

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

for i in range(6):
    cls()
    print("Locating"+str(".")*i)
    sleep(0.3)

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = str(j['latitude'])
lon = str(j['longitude'])
country = str(j['country_name'])
ip = str(j['ip'])

print("\n>>> You are present in",country,"located at Lat:",lat,"and Long:",lon,"\n>>> Your IP address is",ip)
print() # because asthetics
