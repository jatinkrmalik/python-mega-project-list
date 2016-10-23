# Page Scraper
# Create an application which connects to a site and pulls out all links, or images, and saves them to a list. 

# Optional: Organize the indexed content and don't allow duplicates. Have it put the results into an easily searchable index file.

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = input("Enter the website url you want to scrap stuff from:\n")
page = urlopen(url)
# page = requests.get(url)
soup = bs(page.read().decode('latin-1', 'ignore'), 'html5lib')

print(soup.select("a"))
