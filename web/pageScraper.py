# Page Scraper
# Create an application which connects to a site and pulls out all links, or images, and saves them to a list. 

# Optional: Organize the indexed content and don't allow duplicates. Have it put the results into an easily searchable index file.

import requests # pip3 install requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs # pip3 install bs4

url = input("Enter the website url you want to scrap stuff from:\n")
page = urlopen(url)
# page = requests.get(url)
soup = bs(page.read())

print(soup.select("a"))
