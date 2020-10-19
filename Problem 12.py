n_max = 1000

# limit is number of divisors we want to calculate up to.
limit = int(input("> "))

# Using sieve of Eratosthenes, A gives the set of values between 0 and n_max which are prime, stored in a boolean array.
A = [True for i in range(n_max)]

def prime_sieve():
    
    # Eliminating all multiples of 2, 3, etc. up to sqrt(n)
    i = 2
    while i*i <= n_max:
        if A[i] == True:
            for j in range(2*i, n_max, i):
                A[j] = False
        i += 1
    A[0] = False
    A[1] = False

# Calculates the number of factors of input number n
def num_factors(n):
    
    count = 0
    contribution = 1
    for i in range(2,n_max):
        # introducing local variable m = n
        m = n
        if A[i] and m % i == 0:
                # Here we calculate the multiplicity of the relevant prime factors, given by count.
                while m % i == 0:
                    m = m / i
                    count += 1
                contribution = contribution*(count+1)
        else:
            continue
    # We return the product of prime factors exponentiated by their multiplicities (this is the same as the product of all factors).
    return contribution

n = 2

num = 3

prime_sieve()

# We loop through each triangle number, given by n(n-1)/2 and calculate the number of divisors by implementing num_factors on (n) ((n-1)/2) or (n-1) (n/2) depending on whether n is odd or even respectively. 
while num < limit:
    n += 1
    if n % 2 == 0:
        num = num_factors(int(n/2))*num_factors(n+1)
    else:
        num = num_factors(n)*num_factors(int((n+1)/2))

# We return the final triangle number.
print(int(n*(n+1)/2))

