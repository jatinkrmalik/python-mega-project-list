# Fast Exponential
# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.

def fastExp(base, power): # Complexity of O(log n) via Divide & Conquer
    if power == 0:
        return 1

    temp = fastExp(base, power//2)

    if power % 2 == 0:
        return temp*temp

    else:
        if power > 0:
            return base*temp*temp
        else: # To take care of negative power
            return (temp*temp)/base

def conventionalExp(base, power): # Complexity of O(n)
    result = 1
    for i in range(power):
        result = result*base
    print(result)

while(True):
    print("\n\t\tWelcome to Fast Exponential\n")
    base = int(input("Enter the base number: "))
    power = int(input("Enter the exponential power: "))
    print("\nYour answer is: "+str(fastExp(base, power)))
    input("\nPress enter to continue...")

    
