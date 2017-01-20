# Port Scanner 
# Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.


import os

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

while(True):
    cls()
    print("\t\tPort Scanner\n")

    ch = input("(L)ist my open ports\n(S)can for an open port\n(Q)uit\n\n>>>Enter your choice: ").lower()

    if ch == "l":
        print("\n\n# All open ports on this machine are:\n\n")
        os.system("netstat -lntu")

    elif ch == "s":
        print("Todo Port scan")

    elif ch == "q":
        exit()

    else:
        print("\n\nWrong choice entered!\n")       
        
    input("\n\nPress <Enter> to try again or Ctrl+Z to exit")
