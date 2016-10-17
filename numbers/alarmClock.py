# Alarm Clock
# A simple clock where it ~~plays a sound~~ displays a banner after X number of minutes/seconds or at a particular time.

import os
from time import sleep
from random import randint

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def alarm(aSecs):
    aSecs = int(aSecs)    
    for i in range(aSecs):
        cls()
        print("*****************************")
        print("Seconds until alarm: ",aSecs)
        print("*****************************")
        sleep(1)
        aSecs -= 1
    
    while(True):
        for i in range(randint(1,100)):
            print("#", end = "")
        print()
        
print("\n\t\tAlarm Clock/Countdown")

ch = input("Set a alarm based on:\n(A)fter X minutes/seconds\n(C)ustom time\n\n>>>Enter your choice: ").lower()

if ch == "a":
    aT = input("Enter the time-after followed by 'm'/'s' for minutes or seconds respectively: ")
    aTime = aT[:-1]
    aUnit = aT[-1].lower()
    aSecs = 0
    if aUnit == "m":
        aSecs = int(aTime)*60
    else:
        aSecs = aTime
    alarm(aSecs)


