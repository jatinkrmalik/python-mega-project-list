# Credit Card Validator
# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number.

# We will use Luhn Algorithm to validate the card. Read more @ https://en.wikipedia.org/wiki/Luhn_algorithm

def validateCC(cc):
    # Do the magic here

print("\n\t\tCredit card validator\n")
cc = input("Enter your credit card number :")
cc = cc.replace(" ","") # To remove spaces if CC number added like - 5342 3423 2342

if(cc.isnumeric()):
    # Call function here

else:
    print("Invalid characters, please only enter the credit card number!")



