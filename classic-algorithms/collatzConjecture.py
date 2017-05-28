"""
Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""

def collatz_function(input_num, count):
    """Function for computing collatz conjecture"""
    if input_num == 1:
        #if input is 1 print the count
        print('Total steps taken are: ', count)
        return
    elif input_num % 2 == 0:
        #if input is even number divide by 2 and count plus one
        return collatz_function(input_num/2, count+1)
    else:
        #if input is odd number multiply 3 plus 1 and increment count
        return collatz_function(input_num*3+1, count+1)

def main():
    """Game code for keep running the game till user wants."""
    restart = True
    while restart:
        print("\n\t\tLet's play Collatz Conjecture\n")
        input_num = int(input("Enter a number: "))
        collatz_function(input_num, 0)
        #restart if empty string or enter is only pressed else quit.
        restart = input("\nPress enter to continue...") == ''

main()
