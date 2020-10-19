# Using sieve of Eratosthenes, this works out all of the prime numbers under an input number n.
def prime_sieve(n):
    A = [True for i in range(n)]
    i = 2
    while i*i <= n:
        if A[i] == True:
            for j in range(2*i, n, i):
                A[j] = False
        i += 1
    A[0] = False
    A[1] = False
    prime = []
    for p in range(n):
        if A[p]:
            prime.append(p)
    return(prime)

# y stores the values of 600851475143 that are divisible by primes.
y = []

# Calculating the prime numbers less than 2,000,000
for j in range(1000):

    # x gives the prime numbers under 1000 + j.
    x = prime_sieve(10000+j)

    for i in x:
        600851475143 % i and y.append(i)
    
    # We work out the product of all of the prime factors worked out in the previous subroutine. If the answer matches the 600851475143, we break the loop. Else we extend the range.
    prod = 1
    for i in y:
        prod = prod*i

    if prod == 600851475143:
        break
    else:
        continue

