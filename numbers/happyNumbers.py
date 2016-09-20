# Happy Numbers

# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

def amIHappy(num):
    unhappy=[4, 16, 37, 58, 89, 145, 42, 20]

print("\n\t\tHappy Numbers Mining\n")
num = int(input("How many happy numbers do you want: "))

