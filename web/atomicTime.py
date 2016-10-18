# Atomic time
# This program will get the true atomic time from an atomic time clock on the Internet.

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

page = urlopen("https://www.timeanddate.com/worldclock/fullscreen.html?n=4757") # timeanddate.com allows non-commercial scrapping so..

soup = bs(page, "html5lib")

atomicTime =  soup.select("#i_time")[0].get_text()

print("\nAtomic time UTC : ",atomicTime,"\n")
