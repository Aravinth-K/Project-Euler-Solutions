# Finds the sum of divisors by brute force.
def div(n):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
        else:
            continue
    return 1 + sum(factors)

# amicable numbers are those which are involutive under div, i.e. div(div(a)) = a
total = 0
for i in range(2,10000):
    if div(div(i)) == i and div(i) != i:
        total += i
    else:
        continue

print(total)
