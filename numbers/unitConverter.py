# Unit Converter
# Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

def cls(): # to clear the screen
        os.system('cls' if os.name=='nt' else 'clear')

while(True):
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



    

