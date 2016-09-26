# Collatz Conjecture
# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz(num):
    count = 0

    while(num != 1):
        count = count+1
        print("\nStep #"+str(count))
        if(num%2 == 0): # when number is Even
            print(str(num)+" is EVEN, hence num/2")
            num = num//2
        else: # when number is Odd
            print(str(num)+" is ODD, hence (num*3)+1")
            num = (num*3)+1

        print(">>> Now the number = "+str(num))

    print("\nTotal number of steps = "+str(count))

while(True):
    print("\n\t\tLet's play Collatz Conjecture\n")
    num = int(input("Enter a number: "))
    collatz(num)
    input("\nPress enter to continue...")
