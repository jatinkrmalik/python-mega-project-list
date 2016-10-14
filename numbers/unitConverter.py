# Unit Converter
# Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

import os

def cls(): # to clear the screen
        os.system('cls' if os.name=='nt' else 'clear')

# Defining functions

def tempConv():
    cls()
    print("\n\tTemperature Converter\n")

def lenConv():
    cls()
    print("\n\tLength Converter\n")

def areaConv():
    cls()
    print("\n\tArea Converter\n")

def volConv():
    cls()
    print("\n\tVolume Converter\n")

def currConv():
    cls()
    print("\n\tCurrency Converter\n")


while(True):
    cls()
    print("\n\t\tWelcome to Unit converter\n")
    ch = input("(T)emperature\n(L)ength\n(A)rea\n(V)olume\n(C)urrency\n(Q)uit\n\n>>Enter your choice: ").lower()

    if ch == "t":
        tempConv()

    elif ch == "l":
        lenConv()

    elif ch == "a":
        areaConv()

    elif ch == "v":
        volConv()

    elif ch == "c":
        currConv()

    elif ch == "q":
        break
    
    else:
        print("\nWrong choice entered, please try again!")

    input("\nPress enter to continue...")

    

