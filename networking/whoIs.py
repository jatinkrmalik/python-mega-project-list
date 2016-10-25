# Whois Search Tool
# Enter an IP or host address and have it look it up through whois and return the results to you.

import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

# Use https://who.is/whois/<domain> for domain name info
# Use https://who.is/whois-ip/ip-address/<IP ADDRESS> for ip address info

def whoisDom(domain):
    print("Fetching information for",domain)
    domPage = urlopen("https://who.is/whois/"+str(domain))
    soup = bs(domPage, "html5lib")

    print("\n# Registrar Info:")
    key = soup.select(".queryResponseBodyKey")
    val = soup.select(".queryResponseBodyValue")

    for i in range(4):
        print(">>>",key[i].get_text(), end=":")
        print(val[i].get_text())

    print("\n# Important Dates:")
    
    for i in range(4,7):
        print(">>>",key[i].get_text(), end=":")
        print(val[i].get_text())

    print("\n# Name Servers:")
    print(">>>",val[7].get_text(),":", val[8].get_text())
    print(">>>",val[9].get_text(),":", val[10].get_text())
    
    # to continue x = $(".queryResponseBodyValue") in console and check index for Registrar Data
`   return 0

def whoisIP(ipadr):
    print("Fetching information for",ipadr)
    # do magic here
    return 0

while(True):
    cls()
    print("\n\t\tWhois Search Tool\n")
    ch = input("Search by:\n(D)omain name\n(I)P address\n\n>>> Please enter your choice: ").lower()

    if ch == "d":
        print("\nSearch whois information by Domain name:")
        domain = input(">>> Enter the domain name followed by the suffix (.com/.io):\n>>> ")
        whoisDom(domain)
        break

    elif ch == "i":
        print("\nSearch whois information by IP address:")
        ipadr = input(">>> Enter the IP address:\n")
        whoisIP(ipadr)
        break

    else:
        print("\n\nWrong choice entered!")

    input("Press <Enter> to try again or Ctrl+Z to exit")

