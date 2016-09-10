# Have the program find prime numbers until the user chooses to stop asking for the next one.

from math import *
from time import sleep

def findPrimeTillInfinity():
    init = 2
    while(1):
        flag=0
        for j in range(2,int(init)):
            if init%j == 0:
                flag=1
        if flag==0:
            print(init, end="\t", flush=True)
            sleep(0.3)

        init=init+1


print("\nPrime Mining!\n")
findPrimeTillInfinity() # Press CTRL+C to exit
