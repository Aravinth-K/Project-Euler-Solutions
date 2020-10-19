# Calculates the n! taking the lowest number (1) and the largest number (n) and successively evaluating the product of high and low numbers, and then the product of those numbers, such that we never work with an incredibly large number multiplying a small number. 
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def factorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

# Evaluates the sum of digits by incrementing s by the digit number, floor dividing by 10, and repeating until n = 0, at which point the while loop terminates.
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

x = factorial(100)

y = sum_digits(x)

# Prints the final value for the sum of digits of 100!.
print(y)
