# Happy Numbers

# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

from time import sleep

def amIHappy(num):
    unhappy=[4, 16, 37, 58, 89, 145, 42, 20]
    
    for i in range(1,num+1):
        if i in unhappy:
            continue
        else:
            x = i
            sos = 0 # sum of sqaures
        while(True):
            if(x>9):
                temp = x%10
                x = x//10
                sos = sos + pow(temp,2)
            else:
                sos = sos + pow(x,2) # for the last remaining single digit
                x = sos 
                sos = 0 # init sum of squares back to 0 to store for the new compond number
                if(x == 1):
                    print(i, end="\t", flush=True)
                    sleep(0.3) # for dramatic print
                    break
                elif(x in unhappy):
                    break
while(True):
    print("\n\t\tHappy Numbers Mining\n")
    num = int(input("How many happy numbers do you want: "))
    print("\n>>> Happy numbers till "+str(num)+" are:\n")
    amIHappy(num)
    input("\n\nPress enter to continue...")
