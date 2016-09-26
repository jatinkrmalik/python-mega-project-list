# Complex Number Algebra
# Show addition, multiplication, negation, and inversion of complex numbers in separate functions. (Subtraction and division operations can be made with pairs of these operations.) 
# Print the results for each operation tested.

def add(a, b):
    print("\nSum = "+str(a+b))

def sub(a, b):
    print("\nDifference = "+str(a-b))

def mul(a, b):
    print("\nProduct = "+str(a*b))

def div(a, b):
    print("\nDivision = "+str(a/b))

def negation(a, b):
    print("Negation is as follows:\n")
    print(str(a)+" = "+str(-a))
    print(str(b)+" = "+str(-b))

def helpme():
    print("\nIn python, you can put 'j' or 'J' after a number to make it imaginary, so you can write complex literals easily:\n2+3J, 5-6J, where 2+3J ~ 2+3i and 5-6J ~ 5-6i\n\nFun fact - 'i' is also used by mathematicians, physicists, and nearly all other scientists. If that isn't confusing enough, some use 'i' to represent the 'positive' square root of one, whereas 'j' is the 'negative' square root of one.")

print("\n\n\tComplex Number Algebra\n")
a = complex(input("Enter the first complex number in x+yj form: "))
b = complex(input("Enter the second complex number in x+yj form: "))
while(True):
    print("\nChoose your operation:")
    print("\n(A)dd\n(S)ubtract\n(M)ultiply\n(D)ivide\n(N)egation\n(H)elp\n(Q)uit")
    ch = input(">> Enter your choice: ").lower().rstrip()

    if ch == "a":
        add(a, b)
    
    elif ch == "s":
        sub(a, b)

    elif ch == "m":
        mul(a, b)
    
    elif ch == "d":
        div(a, b)
    
    elif ch == "n":
        negation(a, b)
    
    elif ch == "h":
        helpme()
    
    elif ch == "q":
        break

    else:
        print("Wrong choice entered!")

    input("\nPress enter to continue...")
