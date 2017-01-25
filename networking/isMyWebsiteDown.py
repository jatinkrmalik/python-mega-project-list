# Site Checker with Time Scheduling
# An application that attempts to connect to a website or server every so many minutes or a given time and check if it is up. If it is down, it will notify you by email or by posting a notice on screen.


# Use whiptail for notice on screen: 
# Example: whiptail --title "Example Dialog" --msgbox "This is an example of a message box. You must hit OK to continue." 8 78

import os
import time
from urllib.request import urlopen
from urllib.error import URLError, HTTPError # for error handling


def checkSite(weburl, timeInt):
    while(True):
        try:
            status = urlopen(weburl).getcode()
        except URLError as e:
            os.system("whiptail --title 'Website is DOWN!' --msgbox 'Press Ok to continue' 8 78")

        except HTTPError as e:
            os.system("whiptail --title 'Website is DOWN!' --msgbox 'Press Ok to continue' 8 78")
            print(e.code)

        else:
            print("Website is UP! - "+str(status))
        
        time.sleep(timeInt)

print("\t\tSite checker with Time Scheduling\n")
weburl = input("Enter the website url you want to check (http://example.com): ")
timeInt = int(input("Enter the Time interval in seconds between each connection attempt: "))

checkSite(weburl, timeInt)
