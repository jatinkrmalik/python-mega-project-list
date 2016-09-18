# Credit Card Validator
# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number.

# We will use Luhn Algorithm to validate the card. Read more @ https://en.wikipedia.org/wiki/Luhn_algorithm

def validateCC(cc):
    sum1 = 0
    sum2 = 0
    evenLst = [] # Even list

    # Reversing the cc number
    cc = cc[::-1]
    
    # Sum of odd digits
    for i in range(1,len(cc),2):
        sum1=sum1+int(cc[i])

    # Operating on even digits
    for i in range(0,len(cc),2):
        evenLst.append(cc[i]*2)

    # Checking for double digits and summing them
    for i, evenNum in enumerate(evenLst):
        if(int(evenNum)>9):
            evenLst[i]=((int(evenNum)%10)+(int(evenNum)//10)) 
            # Only for once needed as max case could be 9x2=18
    
    # Sum of even list
    for el in evenLst:
        sum2 = sum2+int(el)

    if(int(sum1+sum2)%10 == 0):
        print("\n>>> This is a valid credit card")

    else:
        print("\n>>> This is an invalid credit card")


while(True):
    print("\n\t\tCredit card validator\n")
    cc = input("Enter your credit card number :")
    cc = cc.replace(" ","") # To remove spaces if CC number added like - 5342 3423 2342

    if(cc.isnumeric()):
        validateCC(cc)
    else:
        print(">>> Invalid characters, please only enter the credit card number!")
    

    ch = input("\nDo you want to continue (y/n): ")
    if(ch.lower() == 'n'):
        break
    else:
        continue


