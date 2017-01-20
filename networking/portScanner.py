# Port Scanner 
# Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.


import os

def cls(): # to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

while(True):
    cls()
    print("\t\tPort Scanner\n")

    ch = input("(L)ist my open ports\n(S)can for open port(s)\n(Q)uit\n\n>>>Enter your choice: ").lower()

    if ch == "l":
        print("\n\n# All open ports on this machine are:\n")
        os.system("netstat -lntu") 
        # -l = only services which are listening on some port
        # -n = show port number, don't try to resolve the service name
        # -t = tcp ports
        # -u = udp ports

    elif ch == "s":
        ipadr = input("\n\n>>>Please enter the IP address of the computer(press <Enter> for localhost): ")
        if ipadr == "":
            ipadr = "localhost"
        port = input("\n>>>>Please enter the port number or port range(1-8080): ")
        print("\n\n# Here are your results:\n")
        os.system("nc -zv "+ipadr+" "+port)


    elif ch == "q":
        exit()

    else:
        print("\n\nWrong choice entered!\n")       
        
    input("\n\nPress <Enter> to try again or Ctrl+Z to exit")
