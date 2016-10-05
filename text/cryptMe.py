# Vigenere / Vernam / Ceasar Ciphers
# Functions for encrypting and decrypting data messages. Then send them to a friend.

def vigenere(str,mode):
    if mode == "e": # encryption

    elif mode == "d": # decryption

def vernam(str,mode):
    if mode == "e": # encryption

    elif mode == "d": # decryption

def ceasar(str,mode):
    if mode == "e": # encryption
        key = input("Enter the key for ceasar encryption(- for left shift/+ for right shift): ")
        

    elif mode == "d": # decryption

print("\n\t\tSecret messenger\n")
ch = input("(E)ncrypt my message\n(D)ecrypt my message\n(Q)uit\n\n>>>Enter your choice: ")

ch = ch.lower()

if ch == 'e':
    str = input("\n>>> Enter your message: ")
    str = str.lower() # to reduce the complexity
    op = int(input("\nWhat type of cipher would you like to create by encrypting your message?\n1. Vigenere cipher\n2. Vernam cipher\n3. Ceasar cipher\n\n>>>Enter your choice: "))
    
    if op == 1:
       vigenere(str, "e")

    elif op == 2:
        vernam(str, "e")

    elif op == 3:
        ceasar(str, "e")
    
    else:
	    print("Wrong choice entered!")

elif ch == 'd':
    str = input("\nEnter your encrypted cipher: ")
    op = int(input("\nWhat type of cipher do you have to decrypt your message?\n1. Vigenere cipher\n2. Vernam cipher\n3. Ceasar cipher\n\n>>>Enter your choice: "))

    if op == 1:
        vigenere(str, "d")

    elif op == 2:
        vernam(str, "d")

    elif op == 3:
        ceasar(str, "d")
	
    else:
        print("Wrong choice entered!")

else:
    print("Exiting...")
