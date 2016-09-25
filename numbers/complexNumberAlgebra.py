# Complex Number Algebra
# Show addition, multiplication, negation, and inversion of complex numbers in separate functions. (Subtraction and division operations can be made with pairs of these operations.) 
# Print the results for each operation tested.

def add(aR, aI, bR, bI):
    print("\nSum ="+str(aR+bR)+"+"+str(aI+bI)+"i")

while(True):
    print("\n\n\tComplex Number Algebra\n")
    print("Enter the first complex number: \n")
    aR = int(input("Enter the real part of the complex number: "))
    aI = int(input("Enter the imaginary part of the complex number: "))
    print("\nEnter the second complex number: \n")
    bR = int(input("Enter the real part of the complex number: "))
    bI = int(input("Enter the imaginary part of the complex number: "))
    
    print("\n(A)dd\n(S)ubtract\n(M)ultiply\n(D)ivide\n(I)nverse\n(Q)uit")
    ch = input(">> Enter your choice: ").lower().rstrip()

    if ch == "a":
        add(aR, aI, bR, bI)
    
    elif ch == "s":


    elif ch == case "m":

    
    elif ch == case "m":

    
    elif ch == case "i":

    
    elif ch == case "q":

    
    else:
        print("Wrong choice entered!")

    input("\nPress enter to continue...")
