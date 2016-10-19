# Atomic time
# This program will get the true atomic time from an atomic time clock on the Internet.

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

while(True): # to update in real time
    page = urlopen("https://www.timeanddate.com/worldclock/fullscreen.html?n=4757") # timeanddate.com allows non-commercial scrapping so..
    soup = bs(page, "html5lib") # creating a beautiful soup object
    atomicTime =  soup.select("#i_time")[0].get_text() # extracting atomic time from page
    cls()
    print("\n>>>Atomic time UTC : ",atomicTime,"\n")

