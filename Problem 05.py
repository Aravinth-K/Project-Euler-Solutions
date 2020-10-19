# Import a new type which allows for finding intersections using the & operator.
from collections import Counter

# Function which calculates all factors of the input number.
def factors(n):
    x = []
    for i in range(n+1):
        if i == 0:
            continue
        else:
            n % (i) == 0 and x.append(i)
    return x

# Takes input number and determines whether it is prime.
def primeQ(n):
    y = factors(n)
    if len(y) != 2:
        z = False
    else:
        z = True
    return z

# Computes the prime factors of the input number.
def prime_factors(n):
    x = []
    y = factors(n)
    for i in y:
        primeQ(i) and x.append(i)
    return x

# Calculates the pr
def factorisation(n):
    x = 1
    y = prime_factors(n)

    # x gives the product of prime factors of n.
    for i in y:
        x = x*i
    
    # We successively divide the input number by x, find the prime factors, add those to the list of prime factors in y, and iterate until we have a complete prime factorisation.
    while x != n:
        z = n//x
        w = prime_factors(z)
        y = y + w
        for j in w:
            x = x*j
    return y

print("Input the factors up to which you wish to compute.")

n = int(input("> "))

n_factors = factorisation(1)

# We work out the union of prime factorisations of numbers from 1 up to n. These are then output into factors.
for i in range(2,n+1):
    intersection = list((Counter(n_factors) & Counter(factorisation(i))).elements())
    removed = factorisation(i)
    if len(intersection) == 0:
        n_factors = n_factors + removed
        continue
    else:
        for j in intersection:
            removed.remove(j)
        n_factors = n_factors + removed

# The product of these prime factors gives the smallest positive number evenly divisible by all of the numbers from 1 to n.
num = 1

for i in n_factors:
    num = num*i

print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {n} is {num}")    
