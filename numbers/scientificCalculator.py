# Calculator
# A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

from math import *

# Defining calculator's function(s), feel free to suggest more.
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a//b

def mod(a,b):
    return a%b

def sqaure(a):
    return a*a

def cube(a):
    return a*a*a

def sine(angle):
    return sin(radians(angle))

def cosine(angle):
    return cos(radians(angle))

def tangent(angle):
    return tan(radians(angle))

def power(a,b):
    return pow(a,b)

while True:
    # Calculator menu
    print("\nCalculator\n\n(A)dd\n(S)ubtract\n(M)ultiply\n(D)ivide\n(Mo)dulus\n(Sq)uare\n(Cu)be\n(Si)n\n(Co)s\n(Ta)n\n(P)ower\n(Q)uit")
    choice =input(">>> ").lower().rstrip()
    if choice=="q":
        break
    elif choice=="a":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print(">>> Sum of "+str(a)+" and "+str(b)+" is : "+str(sum(a,b)))
        input("\nPress enter to continue...")

    elif choice=="s":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print(">>> Difference of "+str(a)+" and "+str(b)+" is : "+str(sub(a,b)))
        input("\nPress enter to continue...")

    elif choice=="m":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print(">>> Product of "+str(a)+" and "+str(b)+" is : "+str(mult(a,b)))
        input("\nPress enter to continue...")

    elif choice=="d":
        a=int(input("Enter the Divident: "))
        b=int(input("Enter the Divisor: "))
        print(">>> Division of "+str(a)+" and "+str(b)+" is : "+str(div(a,b)))
        input("\nPress enter to continue...")

    elif choice=="mo":
        a=int(input("Enter the Divident: "))
        b=int(input("Enter the Divisor: "))
        print(">>> Modulus of "+str(a)+" and "+str(b)+" is : "+str(mod(a,b)))
        input("\nPress enter to continue...")

    elif choice=="sq":
        a=int(input("Enter the number: "))
        print(">>> Square of "+str(a)+" is : "+str(sqaure(a)))
        input("\nPress enter to continue...")

    elif choice=="cu":
        a=int(input("Enter the number: "))
        print(">>> Cube of "+str(a)+" is : "+str(cube(a)))
        input("\nPress enter to continue...")

    elif choice=="si":
        angle=int(input("Enter the angle: "))
        print(">>> Sine value of angle "+str(angle)+" is : "+str(sine(angle)))
        input("\nPress enter to continue...")

    elif choice=="co":
        angle=int(input("Enter the angle: "))
        print(">>> Cosine value of angle "+str(angle)+" is : "+str(cosine(angle)))
        input("\nPress enter to continue...")

    elif choice=="ta":
        angle=int(input("Enter the angle: "))
        print(">>> Tangent value of angle "+str(angle)+" is : "+str(tangent(angle)))
        input("\nPress enter to continue...")

    elif choice=="p":
        a=int(input("Enter the base: "))
        b=int(input("Enter the power: "))
        print(">>> Value of base "+str(a)+" for exponent "+str(b)+" is : "+str(pow(a,b)))
        input("\nPress enter to continue...")

    else:
        print("Invalid choice, please choose again!\n")

print("\nThank you for using the calculator")

