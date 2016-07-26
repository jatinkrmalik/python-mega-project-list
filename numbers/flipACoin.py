# Coin Flip Simulation
# Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

from random import randint

def coinFlip(numFlip):
    numHead = 0
    numTail = 0

    for i in range(numFlip):
        result = randint(0,1)

        if result == 0: # 0 is head
            numHead += 1 
        else: # 1 is tail
            numTail += 1

    print("\nFor "+str(numFlip)+" flips of a coin, here are the results:")
    print("\n>>> Number of Heads = "+str(numHead))
    print(">>> Number of Tails = "+str(numTail))
    print() # because asthetics!

print("\n\t\tCoin flip simulation\n")
numFlip = int(input("How many times do you want to flip the coin: "))
coinFlip(numFlip)
