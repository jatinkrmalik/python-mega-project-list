# Tax Calculator
# Asks the user to enter a cost and state tax. It then returns the tax plus the total cost with tax.

def calcTax(cost,tax):
    taxC = cost*(tax/100) # calculating tax
    return taxC,cost+taxC # returning both tax and total amount

print("\n\t\tTax Calculator\n")
cost = int(input("\nPlease enter the cost of the item: INR "))
tax = float(input("\nPlease enter the tax (in %): "))

print("\n>>> Tax calucated on the item is: INR "+str(calcTax(cost,tax)[0]))
print("\n>>> Total amount is: INR "+str(calcTax(cost,tax)[1]))
print() # because asthetics!


