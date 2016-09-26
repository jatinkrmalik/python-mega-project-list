# Sieve of Eratosthenes
# The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).

# To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
# 2. Initially, let p equal 2, the smallest prime number.
# 3. Enumerate the multiples of p by counting to n from 2p in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
# 4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.

def eratosthenes(num):
    primes = list(range(2, num)) # One is neither a prime nor a composite number.
'''    for num in prime:
        if(num%i==0):
            prime.pop(i)
''' # Do the magic here ^

print("\n\t\tEfficient Prime Mining\n")
num = int(input("Enter a number to search for primes till that range (<10mn): "))
eratosthenes(num)

# Sift the Two's and Sift the Three's,
# The Sieve of Eratosthenes.
# When the multiples sublime,
# The numbers that remain are Prime
# - Anonymous
