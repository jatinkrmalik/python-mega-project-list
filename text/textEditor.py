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

ch = input("\n-------\n(O)pen a new file\n(E)dit an exiting file\n(Q)uit\n>>>Enter your choice: ").lower()

if ch == "o":
    cls() # to clear the screen
    plainText = input("Enter your text below:\n\n")
    _ch = input("\n--------\n(S)ave file\t(Q)uit without saving\n>>>Enter your choice: ").lower()
    
    if _ch == "s":
        fileName = input("Enter your file name: ")
        fo = open(fileName+".txt", "wb")
        fo.write(bytes(plainText, 'UTF-8'))
        fo.close()

    elif _ch == "q":
        exit()

if ch == "e":
    fileName = input("Enter the name of file you want to open: ")
    fo = open(fileName+".txt", "rb")
    cls()
    print("Content of "+fileName+" is:\n--------\n")
    print(fo.read())
    fo.close()
    _ch = input("\n--------\n(E)dit this file\t(Q)uit\n>>>Enter your choice: ").lower()

    if _ch == "e":
        plainText = input("Enter the text you want to add below:\n\n")
        fo = open(fileName+".txt", "ab+")
        fo.write(bytes(" "+plainText, 'UTF-8'))
        print("\nUpdated content of file is: \n")
        fo.seek(0)
        print(fo.read())
        fo.close()

    elif _ch == "q":
        exit()


