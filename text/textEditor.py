# Text editor
# Notepad style application that can open, edit, and save text documents. Optional: Add syntax highlighting and other features.

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("\n\t\tText Editor\n")

try: # to check if directory exists
    os.mkdir("documents")
    os.chdir("documents")
except FileExistsError:
    os.chdir("documents")

ch = input("(O)pen a new file\n(E)dit an exiting file\n(Q)uit\n>>>Enter your choice: ").lower()

if ch == "o":
    cls() # to clear the screen
    str = input("Enter your text below:\n\n")
    _ch = input("\n--------\n(S)ave file\n(Q)uit without saving\n>>>Enter your choice: ").lower()
    
    if _ch == "s":
        fileName = input("Enter your file name: ")
        fo = open(fileName+".txt", "wb")
        fo.write(str)
        fo.close()

    elif _ch == "q":
        exit()
     
