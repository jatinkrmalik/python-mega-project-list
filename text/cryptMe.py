# Vigenere / Vernam / Ceasar Ciphers
# Functions for encrypting and decrypting data messages. Then send them to a friend.


alphaList = []
j = 65 # for ascii
for i in range(26):
    alphaList.append(chr(j)) # populating list with alphabets
    j += 1

"""def vigenere(str,mode):
    if mode == "e": # encryption

    elif mode == "d": # decryption

def vernam(str,mode):
    if mode == "e": # encryption

    elif mode == "d": # decryption
"""


def ceasar(str,mode): # To imporve the acceptance of both upper and lower case
    op = ""
    if mode == "e": # encryption
        key = int(input("Enter the key for ceasar encryption: "))
        for i in range(len(str)):
            if ord(str[i])>64 and ord(str[i])<91:
                op = op+alphaList[int(alphaList.index(str[i])+key)%26]
            else:
                op = op+str[i]
        print("\nCeaser cipher for your message = ",op)
        
    elif mode == "d": # decryption
        key = int(input("Enter the key to decrypt the ceasar cipher: "))
        for i in range(len(str)):
            if ord(str[i])>64 and ord(str[i])<91:
                op = op+alphaList[int(alphaList.index(str[i])-key)%26]
            else:
                op = op+str[i]
        print("\nCeaser decryption for your message = ",op)


print("\n\t\tSecret messenger\n")
ch = input("(E)ncrypt my message\n(D)ecrypt my message\n(Q)uit\n\n>>>Enter your choice: ")
ch = ch.lower()

if ch == 'e':
    str = input("\n>>> Enter your message to encrpyt: ")
    str = str.upper() # to reduce the complexity
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
    str = input("\nEnter your encrypted cipher to decrypt: ").upper()
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
