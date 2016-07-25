# Binary to Decimal and back convertor
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def dec2bin(decnum):
    binnum = ""
    while decnum != 1:
        binnum = binnum+str(decnum%2)
        decnum = int(decnum/2)
    binnum = binnum+"1"
    print(">>> ", end="")
    print(binnum[::-1])

def bin2dec(binnum):
    temp = binnum
    decnum = 0
    for i in range(len(str(binnum))):
        decnum = decnum + pow(2,i)*(temp%10)
        temp=temp//10
    print(">>> ", end="")
    print(decnum)

while True:
    print("\n\t\tBinary to Decimal to Binary\n\n(D) Decimal to Binary\n(B) Binary to Decimal\n(Q) Quit")
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


