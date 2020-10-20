import time

start = time.time()

# Finds the sum of divisors by brute force.
def div(n):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
        else:
            continue
    return 1 + sum(factors)

# abundant numbers are those for which the divisor is greater than the number itself.
abundant_numbers = []
for i in range(2,28124):
    if div(i) > i:
        abundant_numbers.append(i)
    else:
        continue

print(abundant_numbers[50])

print(len(abundant_numbers))


end = time.time()

print(end - start)
