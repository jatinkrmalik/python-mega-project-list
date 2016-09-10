# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fibo(n):
    # Initialising 2 counters
    pres=1
    prev=0
    for i in range(1,n):
        if prev==0:
            print(1, end=' ')
        temp=prev+pres
        prev=pres
        pres=temp
        print(temp, end=' ')
    print() # Empty line because 'asthethics'

print("\n\t\tFibonacci sequence\n")

length = int(input("\nEnter a number to generate Fibonacci series upto that length : "))

print("\nFibonacci series upto "+str(length)+" length is :\n")

fibo(length)
