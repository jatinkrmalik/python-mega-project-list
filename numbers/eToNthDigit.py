# Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

from math import *
from decimal import *

def calcE():
    e = Decimal(1)
    for i in range(1,1000):
        e = e + Decimal(1/factorial(i)) # Calculating e using Taylor's series
    return e

print("\n\t\te Calculator")

while(1):
    length = int(input("\nEnter a number to generate e up to that many decimal places : "))
    getcontext().prec = length+1

    if(length<=100): # Max limit of 100 decimal places
        break

    else:
        print("\nNumber should be less than 100")

print("Value of e upto "+str(length)+" digits is : "+str(round(calcE(),length))) # Rounding off to nearest decimal
