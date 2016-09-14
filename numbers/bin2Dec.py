# Binary to Decimal and back convertor
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def dec2bin(decnum):
    binnum = ""
    while decnum != 1:
        binnum = binnum+str(decnum%2)
        decnum = int(decnum/2)
    binnum = binnum+"1"
    print(binnum[::-1])

def bin2dec(binnum):
    binlen = len(binnum)

#    for i in range(binnum):
        # write logic here


while True:
    print("\nBinary to Decimal to Binary\n(D) Decimal to Binary\n(B) Binary to Decimal\n(Q) Quit")
    choice =input(">>> ").lower().rstrip()
    if choice=="q":
        break
    elif choice=="d":
        decnum = int(input("Enter a decimal number to convert it to binary: "))
        dec2bin(decnum)
    elif choice=="b":
        binnum = int(input("Enter a binary number to convert it to decimal: "))
        bin2dec(binnum)
    else:
        print("Invalid choice, please choose again!\n")

print("Thank you")


