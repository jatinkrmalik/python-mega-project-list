# Tax Calculator
# Asks the user to enter a cost and state tax. It then returns the tax plus the total cost with tax.

def calcTax(cost,tax):
    return cost+(cost*tax/100)

print("\n\t\tTax Calculator\n")
cost = int(input("\nPlease enter the cost of the item: INR "))
tax = float(input("\nPlease enter the tax (in %): "))

print("\n>> Total amount is: INR "+str(calcTax(cost,tax)))
print() # because asthetics!
