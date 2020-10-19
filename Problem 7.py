# Obviously primeQ can be answered by just seeing if it was divisible by primes, rather than all numbers. Obviously.

def nth_prime(n):
    # We generate a list of prime numbers called primes.
    primes = [2]
    i = 3

    # Starting from i and increasing by one each time, we work out whether the number is prime and add it to prime until we have n primes.
    while len(primes) < n:

        k = []

        for j in primes:

            if i % j == 0:
                k.append(j)
            else:
                continue
        
        len(k) == 0 and primes.append(i)
        
        i += 1

    # We return the last prime.
    return primes[-1]

print("Input the number you wish to go up to.")

m = int(input("> "))

print(f"The {m}th prime is {nth_prime(m)}")
