# Vigenere / Vernam / Ceasar Ciphers
# Functions for encrypting and decrypting data messages. Then send them to a friend.


alphaList = []
j = 65 # for ascii
for i in range(26):
    alphaList.append(chr(j)) # populating list with alphabets
    j += 1


# Pending encryptions, will come back after some research
"""def vigenere(msg,mode):
    if mode == "e": # encryption

    elif mode == "d": # decryption

def vernam(msg,mode):
    if mode == "e": # encryption

    elif mode == "d": # decryption
"""


def ceasar(msg,mode): # To imporve the acceptance of both upper and lower case
    op = ""
    if mode == "e": # encryption
        key = int(input("\n>>>Enter the key for ceasar encryption: "))
        for i in range(len(msg)):
            if ord(msg[i])>64 and ord(msg[i])<91:
                op = op+alphaList[int(alphaList.index(msg[i])+key)%26]
            else:
                op = op+msg[i]
        print("\nCeaser cipher for your message = ",op)
        
    elif mode == "d": # decryption
        ch = input("\nDo you want to decrypt using :\n(K)ey\n(B)rute force method\n\n>>>Enter your choice: ")
        if ch.lower() == "k":
            key = int(input("Enter the key to decrypt the ceasar cipher: "))
            for i in range(len(msg)):
                if ord(msg[i])>64 and ord(msg[i])<91:
                    op = op+alphaList[int(alphaList.index(msg[i])-key)%26]
                else:
                    op = op+msg[i]
            print("\nCeaser decryption for your message = ",op)

        else:
            print("\nAttemping Brute force on:\n>>>",msg,end="\n\n")
            for key in range(26):
                op = ""
                for i in range(len(msg)):
                    if ord(msg[i])>64 and ord(msg[i])<91:
                        op = op+alphaList[int(alphaList.index(msg[i])-key)%26]
                    else:
                        op = op+msg[i]

                print("Key = ",'{:2}'.format(key),"| Message = ", op)

print("\n\t\tSecret messenger\n")
ch = input("(E)ncrypt my message\n(D)ecrypt my message\n(Q)uit\n\n>>>Enter your choice: ")
ch = ch.lower()

if ch == 'e':
    msg = input("\n>>> Enter your message to encrpyt: ")
    msg = msg.upper() # to reduce the complexity
    op = int(input("\nWhat type of cipher would you like to create by encrypting your message?\n1. Vigenere cipher\n2. Vernam cipher\n3. Ceasar cipher\n\n>>>Enter your choice: "))
    
    if op == 1:
       vigenere(msg, "e")

    elif op == 2:
        vernam(msg, "e")

    elif op == 3:
        ceasar(msg, "e")
    
    else:
	    print("Wrong choice entered!")

elif ch == 'd':
    msg = input("\nEnter your encrypted cipher to decrypt: ").upper()
    op = int(input("\nWhat type of cipher do you have to decrypt your message?\n1. Vigenere cipher\n2. Vernam cipher\n3. Ceasar cipher\n\n>>>Enter your choice: "))

    if op == 1:
        vigenere(msg, "d")

    elif op == 2:
        vernam(msg, "d")

    elif op == 3:
        ceasar(msg, "d")
	
    else:
        print("Wrong choice entered!")

else:
    print("Exiting...")

print() # asthetics
