# Whois Search Tool
# Enter an IP or host address and have it look it up through whois and return the results to you.

import os

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

# Use https://who.is/whois/<domain> for domain name info
# Use https://who.is/whois-ip/ip-address/<IP ADDRESS> for ip address info

def whoisDom(domain):
    print("Fetching information for",domain)
    # do magic here
    return 0

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

