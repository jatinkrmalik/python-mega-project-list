# Text editor
# Notepad style application that can open, edit, and save text documents. 
# Optional: Add syntax highlighting and other features.

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

try: # to check if directory exists
    os.mkdir("documents")
    os.chdir("documents")
except FileExistsError:
    os.chdir("documents")

while True:
    print("\n\t\tText Editor")

    ch = input("\n(O)pen a new file\n(E)dit an exiting file\n(Q)uit\n\n>>>Enter your choice: ").lower()

    if ch == "o":
        cls() # to clear the screen
        print("Enter your text below (Press Ctrl+C to escape from editor):\n--------\n")
    
        try:
            textPara = ""
            while True:
                textLine = input()
                textPara = textPara+"\n"+textLine
        except KeyboardInterrupt:
            pass

        _ch = input("\n--------\n\n(S)ave file\t(Q)uit without saving\n\n>>>Enter your choice: ").lower()
    
        if _ch == "s":
            fileName = input("Enter your file name: ")
            fo = open(fileName+".txt", "w+")
            fo.write(textPara)
            fo.close()

        elif _ch == "q":
            exit()

    if ch == "e":
        fileName = input("Enter the name of file you want to open: ")
        fo = open(fileName+".txt", "r+")
        cls()
        print("Content of "+fileName+" is:\n--------")
        print(fo.read())
        fo.close()
        _ch = input("\n--------\n\n(A)dd more text to this file\t(Q)uit\n\n>>>Enter your choice: ").lower()

        if  _ch == "a":
            plainText = input("Enter the text you want to add below:\n")
            fo = open(fileName+".txt", "a+")
            fo.write("\n"+plainText)
            print("\nUpdated content of file is:\n--------")
            fo.seek(0)
            print(fo.read())
            fo.close()

        elif _ch == "q":
            exit()

    elif ch == "q":
        exit()
