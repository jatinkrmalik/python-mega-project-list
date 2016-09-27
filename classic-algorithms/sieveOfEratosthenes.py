# Sieve of Eratosthenes
# The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).

# ALGORITHM:
# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
# 2. Initially, let p equal 2, the smallest prime number.
# 3. Enumerate the multiples of p by counting to n from 2p in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
# 4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.

def eratosthenes(limit):
    primeLst = [False] * 2 + [True] * (limit - 1) # Creating a list with flags to identify Prime or not
    for n in range(int(limit**0.5)): # stop at sqrt(limit)
        if primeLst[n]:
            for i in range(n * n, limit + 1, n): # Starting loop at n^2, to avoid checking for numbers that are already evaluated.
                primeLst[i] = False
    for i in range(limit + 1):
        if primeLst[i]:
                print(i, end="\t")


("\n\t\tEfficient Prime Mining\n")
limit = int(input("Enter a number to search for primes till that range (<10mn): "))
print("Here are your prime numbers :\n")
eratosthenes(limit)
print()

# ------------------------------------
# Sift the Two's and Sift the Three's,
# The Sieve of Eratosthenes.
# When the multiples sublime,
# The numbers that remain are Prime
#                        -- Anonymous
# -----------------------------------
