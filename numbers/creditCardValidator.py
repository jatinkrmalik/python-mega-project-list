# Credit Card Validator
# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number.

# We will use Luhn Algorithm to validate the card. Read more @ https://en.wikipedia.org/wiki/Luhn_algorithm

# Some sample CC numbers to verify:
#   Visa                4111 1111 1111 1111 
#   MasterCard          5500 0000 0000 0004 
#   American Express    3400 0000 0000 009 
#   Diner's Club        3000 0000 0000 04 
#   Carte Blanche       3000 0000 0000 04 
#   Discover            6011 0000 0000 0004 
#   en Route            2014 0000 0000 009 
#   JCB                 3088 0000 0000 0009 

def validateCC(cc):
    sum1 = 0
    sum2 = 0
    evenLst = [] # Even list

    # Reversing the cc number
    cc = cc[::-1]
    
    # Sum of odd digits
    for i in range(0,len(cc),2):
        sum1=sum1+int(cc[i])

    # Operating on even digits
    for i in range(1,len(cc),2):
        evenLst.append(int(cc[i])*2)

    # Checking for double digits and summing them
    for i, evenNum in enumerate(evenLst):
        if(int(evenNum)>9):
            evenLst[i]=(evenNum%10)+(evenNum//10) # equivalent to divmod
            # Only for once needed as max case could be 9x2=18
    
    # Sum of even list
    sum2=sum(evenLst)
# Only for debugging- print("Sum is :"+str(sum1)+" + "+str(sum2)+" = "+str(sum1+sum2))

    if(int(sum1+sum2)%10 == 0):
        print("\n>>> This is a valid credit card")

    else:
        print("\n>>> This is an invalid credit card")


while(True):
    print("\n\t\tCredit card validator\n")
    cc = input("Enter your credit card number :")
    cc = cc.replace(" ","") # To remove spaces if CC number added like - 5342 3423 2342 1234

    if(cc.isnumeric()): # To make sure only numericals are entered
        validateCC(cc)
    else:
        print(">>> Invalid characters, please only enter the credit card number!")
    
    ch = input("\nDo you want to continue (y/n): ")
    if(ch.lower() == 'n'):
        break
    else:
        continue


