# Caesar Cipher
# Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet(wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.

alphaList = []
j = 65 # for ascii
for i in range(26):
    alphaList.append(chr(j)) # populating list with alphabets
    j += 1

def ceasar(msg,mode): 
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
    ceasar(msg, "e")
    
elif ch == 'd':
    msg = input("\nEnter your encrypted cipher to decrypt: ").upper()
    ceasar(msg, "d")
	
else:
    print("Exiting...")

print() # asthetics
