from decimal import *

print("\n\t\tPI Calculator")

while(1):
    length = int(input("\nEnter a number to generate PI up to that many decimal places : "))
    getcontext().prec = length+1

    if(length<100):
        break

    else:
        print("\nNumber should be less than 100")

print("Value of PI upto "+str(length)+" digits is : "+str(Decimal(355)/Decimal(113)))

# I know this is not the best way to calculate the value of Pi, I will revisit this after some research
