# Calculating 2^100 manually will take a long time. This problem probably wants you to use a more efficient exponentiation algorithm. Exponentiation by squaring is the one I will use.

def exp_by_squaring(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_squaring(x*x, int(n/2))
    else:
        return x*exp_by_squaring(x*x, int((n-1)/2))

# We add the last digit of a number n, then removes that last digit and repeats until the number hits zero, at which point you get 0 = False and the loop terminates.
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_digits(exp_by_squaring(2,1000)))
