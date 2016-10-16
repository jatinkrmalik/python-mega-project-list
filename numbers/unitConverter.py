# Unit Converter
# Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

import os

def cls(): # to clear the screen
        os.system('cls' if os.name=='nt' else 'clear')

# Defining functions

def tempConv():
    cls()
    while(True):
        print("\n\tTemperature Converter\n")
        tempch = input("(1C)elsius to Fahrenheit\n(2C)elsius to Kelvin\n(1F)ahrenheit to Celcius\n(2F)ahrenheit to Kelvin\n(1K)elvin to Celsius\n(2K)elvin to Fahrenheit\n--------\n(B)ack to the main menu\n\n>>Enter your choice: ").lower()
        
        if tempch == "1c":
            cTemp = float(input("\n>>Enter the temperature in Celsius: "))
            fTemp = float((9 * cTemp) / 5 + 32)
            print("\nThe temperature",cTemp,"C =",fTemp,"F")
        
        elif tempch == "2c":
            cTemp = float(input("\n>>Enter the temperature in Celsius: "))
            kTemp = float(cTemp + 273.15)
            print("\nThe temperature",cTemp,"C =",kTemp,"K")
        
        elif tempch == "1f":
            fTemp = float(input("\n>>Enter the temperature in Fahrenheit: "))
            cTemp = float((fTemp - 32) * 5 / 9)
            print("\nThe temperature",fTemp,"F =",cTemp,"C")

        elif tempch == "2f":
            fTemp = float(input("\n>>Enter the temperature in Fahrenheit: "))
            kTemp = float((fTemp + 459.67)* 5 / 9)
            print("\nThe temperature",fTemp,"F =",kTemp,"K")

        elif tempch == "1k":
            kTemp = float(input("\n>>Enter the temperature in Kelvin: "))
            fTemp = float((kTemp * 9 / 5) - 459.67)
            print("\nThe temperature",kTemp,"K =",fTemp,"F")

        elif tempch == "2k":
            kTemp = float(input("\n>>Enter the temperature in Kelvin: "))
            cTemp = float((kTemp - 273.15))
            print("\nThe temperature",kTemp,"K =",cTemp,"C")

        elif tempch == "b":
            break

        else:
            print("\nWrong choice entered, please try again!")

        input("\nPress enter to continue...")

def lenConv():
    cls()
    while(True):
        print("\n\tLength Converter\n")
        unit1 = input ("Which unit would you like to convert from: ")
        unit2 = input ("Which unit would you like to convert to: ")
        num1 = input ("Enter your value: " )

        ##Calculations  
        if unit1 == "cm" and unit2 == "m":
            ans = float(num1)/100       
        elif unit1 == "mm" and unit2 == "cm":
            ans = float(num1)/10
        elif unit1 == "m" and unit2 == "cm":
            ans = float(num1)*100
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num1)*10
        elif unit1 == "mm" and unit2 == "m":
            ans = float(num1)/1000
        elif unit1 == "m" and unit2 == "mm":
            ans = float(num1)*1000  
        elif unit1 == "km" and unit2 == "m":
            ans = float(num1)*1000
        elif unit1 == "m" and unit2 == "km":
            ans = float(num1)/1000
        elif unit1 == "mm" and unit2 == "km":
            ans = float(num1)/1000000
        else:
            print("\nWrong choice entered, please try again!")

        print("\nThe length",num1,unit1,"=",ans,unit2)
        
        rep = input("\nDo you want to continue? (y/n) ").lower()
        if rep == "n":
            break

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

    

