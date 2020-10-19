# Using sieve of Eratosthenes, this function computes the set of prime numbers up to an input number n. The list of prime numbers is returned.
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

print("Enter the bound for the primes you wish to count up to.")

n = int(input("> "))

print(sum(prime_sieve(n)))
