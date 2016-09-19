# Factorial finder
# The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. 

# Note - Solve this using both loops and recursion.


def factViaLoop(num):
    fact = int(1)
    for i in range(1,num+1):
        fact = fact*i
    print("\nFactorial of "+str(num)+" = "+str(fact))
    input("\nPress enter to continue...")

def factViaRec(num):
#    fact = int(1)
#    if(num>=1):
#        fact = num * factViaRec(num-1)
#    print("\nFactorial of "+str(num)+" = "+str(fact))
    input("Press enter to continue...")

while(True):
    print("\n\t\tFactorial Calculator\n")
    num = int(input("Enter the number to find the factorial for: "))
    ch = input("\nFind factorial via:\n(L)oop\n(R)ecursion\n(Q)uit\n>>> ")

    if (ch.lower()=="l"):
        factViaLoop(num)

    elif (ch.lower()=="r"):
        factViaRec(num)

    elif (ch.lower()=="q"):
        break

    else:
        print("\nWrong input. Please try again")


