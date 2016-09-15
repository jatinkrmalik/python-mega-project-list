# Calculator
# A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

from math import *

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
        print(sub(a,b))
 
    elif choice=="m":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print(mult(a,b))
    
    elif choice=="d":
        a=int(input("Enter the Divident: "))
        b=int(input("Enter the Divisor: "))
        print(div(a,b))
    
    elif choice=="mo":
        a=int(input("Enter the Divident: "))
        b=int(input("Enter the Divisor: "))
        print(mod(a,b))

    elif choice=="sq":
        a=int(input("Enter the number: "))
        print(sqaure(a))

    elif choice=="cu":
        a=int(input("Enter the number: "))
        print(cube(a))

    elif choice=="si":
        angle=int(input("Enter the angle: "))
        print(sine(angle))

    elif choice=="co":
        angle=int(input("Enter the angle: "))
        print(cosine(angle))

    elif choice=="ta":
        angle=int(input("Enter the angle: "))
        print(tangent(angle))

    elif choice=="p":
        a=int(input("Enter the base: "))
        b=int(input("Enter the power: "))
        print(pow(a,b))

    else:
        print("Invalid choice, please choose again!\n")

print("\nThank you for using the calculator")

