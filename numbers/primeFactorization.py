# Have the user enter a number and find all Prime Factors (if there are any) and display them.

from math import *

def findPrimeTill(num):
    primeList = []
    for i in range(2,num):
        flag=0
        for j in range(2,int(sqrt(i))):
            if i%j == 0:
                flag=1
        if flag==0:
            primeList.append(i)

    return primeList

def amIPrime(num):
    for i in range(2,num):
        flag=0
        if num%i == 0:
            flag=1
            print()
            print(str(num)+" is not a Prime number, hence calculating it's Prime Factors...\n")
            return False
        if flag==0:
            print()
            print(str(num)+" is a Prime number, hence it's Prime Factors don't exist!\n")
            return True     
        
def findPrimeFactors(num):
    primeList = findPrimeTill(int(num))
    print("\t>>>> Here are the Prime factors of "+str(num)+":", end=' ')
    for i in primeList:
        while num!= 1:
            if num%i == 0:
                print(i, end='')
                num=num/i
                if(num != 1):
                    print(' x ',end='')
            else:
                break
    print('\n') # Empty line

print("\n\t\tPrime Factorization!\n")
num = input("\nEnter a number to find all of it's Prime factors (if any): ")
if(amIPrime(int(num))==False):
    findPrimeFactors(int(num))
