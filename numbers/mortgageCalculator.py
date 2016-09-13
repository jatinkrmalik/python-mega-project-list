# Mortgage Calculator
# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. 

# >>Future scope - For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

from math import *

def calcEMI(loanAmt, rateInt, tenureM):
       emi = ((rateInt/1200)*loanAmt)/((1-pow((1+rateInt/1200),(-tenureM)))) # direct calculation of EMI by using rate of interest per month.
       print("\nMonthly payment = INR "+str(round(emi,2)))
       print("Total amount to be paid = INR "+str(round(emi*tenureM,2)))
       print() # because 'asthetics'!

print("\n\t\tMortgage Calculator\n")

loanAmt = int(input("Enter the Loan amount: INR "))
rateInt = float(input("Enter the Rate of Interest (in %): "))
tenureY = int(input("Enter the tenure of the Loan (in years): "))
tenureM = tenureY*12 # Converting years to month for ease of calculation

calcEMI(loanAmt, rateInt, tenureM)

