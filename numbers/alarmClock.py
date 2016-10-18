# Alarm Clock
# A simple clock where it ~~plays a sound~~ displays a banner after X number of minutes/seconds or at a particular time.

# To-do: Add an option to add a custom date too!

import os
from time import sleep, strftime
from random import randint

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def h2s(t): # to convert 24 hours time into seconds
    h, m, s = [int(i) for i in t.split(':')]
    return 3600*h + 60*m + s

def alarm(aSecs):
    aSecs = int(aSecs)    
    for i in range(aSecs):
        cls()
        print("\n"*randint(0,10))
        print("*****************************")
        print("Seconds until alarm: ",aSecs)
        print("*****************************")
        sleep(1)
        aSecs -= 1
    
    while(True):
        print("#"*randint(1,100)) # to jazz up the screen
                
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

elif ch == "c":
    aT = input("Enter the alarm time in 24 hours format (HH:MM:SS): ")
    cT = strftime("%H:%M:%S") # taking time elapsed in seconds from midnight
    dSecs = 24*60*60

    aTSecs = int(h2s(aT)) # converting 24 hours time to seconds
    cTSecs = int(h2s(cT))

    if cTSecs > aTSecs: # when time has passed, so scheduling for next day
        alarm(dSecs+(aTSecs-cTSecs))

    else:
        alarm(aTSecs-cTSecs)


