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

def whoisDom(domain): # to get whois via domain
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
    print(">>>",val[7].get_text().replace("\n",""),":", val[8].get_text().replace("\n",""))
    print(">>>",val[9].get_text().replace("\n",""),":", val[10].get_text().replace("\n",""))
   
    print("\n# Similar Domains:")
    simDoms = val[11].get_text().replace("\n","").split(" | ")
    for sDom in simDoms:
        print(">>>",sDom) 
   
    print("\n# Registrar Data:")

    # Registrant Contact Information:
    print("\n>>> "+val[12].select(".rawWhois > div > strong")[0].get_text())
    for i in range(20):
        if i%2==0:
            print(val[12].select(".rawWhois .row div")[i].get_text(),end=":")
        else:
            print(val[12].select(".rawWhois .row div")[i].get_text(),end="\n")

    # Administrative Contact Information:
    print("\n>>> "+val[12].select(".rawWhois > div > strong")[1].get_text())
    for i in range(20,40):
        if i%2==0:
            print(val[12].select(".rawWhois .row div")[i].get_text(),end=":")
        else:
            print(val[12].select(".rawWhois .row div")[i].get_text(),end="\n")

    # Technical Contact Information:
    print("\n>>> "+val[12].select(".rawWhois > div > strong")[2].get_text())
    for i in range(20,40):
        if i%2==0:                                                                       
            print(val[12].select(".rawWhois .row div")[i].get_text(),end=":")
        else:
            print(val[12].select(".rawWhois .row div")[i].get_text(),end="\n")

    print("-"*10)
    print(val[12].select(".rawWhois > div")[3].get_text())
    print() # asthetics
    
def whoisIP(ipadr): # to get whois via IP
    print("Fetching information for",ipadr)
    IPPage = urlopen("https://who.is/whois-ip/ip-address/"+str(ipadr))
    soup = bs(IPPage, "html5lib")

    print("\n# IP Whois:")
    key = soup.select(".col-md-12.queryResponseBodyKey > pre")
    print(key[0].get_text())
    print() #asthetics

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

