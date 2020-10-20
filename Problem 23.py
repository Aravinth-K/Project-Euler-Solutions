# We need to implement a function in Python representing the divisor function \sigma_1(n).

n_max = 28124

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

# This function outputs the sum of proper divisors.
def div(n):
    
    contribution = 1
    for i in range(2, n//2):
        # introducing local variable m = n
        m = n
        if A[i] and m % i == 0:
            multiplicity = 0
            # Here we calculate the multiplicity of the relevant prime factors, given by multiplicity.
            while m % i == 0:
                m = m / i
                multiplicity += 1
            # Each divisor can be expressed as a product of functions of the prime factors p_i, (p_i^(mult. +1) - 1)/(p_i - 1), see Intro to theory of numbers, Hard.
            if multiplicity != 1:
               factor = (i**(multiplicity + 1) -1)//(i-1)
               contribution = contribution*factor
            else:
               factor = i + 1
               contribution = contribution*factor
            
        else:
            continue
    # We return the proper divisor, given by contribution minus n.
    return (contribution - n)

# Actually implementing the prime_sieve on A
prime_sieve()

# For all integers between 2 and 28123 we check whether there it can be written as the sum of abundant numbers and store the result if it is not. We only need to check the abundant numbers < n since if n is the sum of two abundant numbers, and each is a positive integer, each must be less than n.

abundant_subspace = set()
answer = 0
for n in range(1, 28124):
    if div(n) > n:
        abundant_subspace.add(n)
    if not any((n - a in abundant_subspace) for a in abundant_subspace):
        answer += n  # accumulate sum

print(answer)

