# This is conceptually simple. For an n x n grid, it's just the number of ways of arranging n d letters and n r letters in a 2n length word. This is just the binomial coefficient binom(2n,n)

n = int(input("> "))

# binom(2n)(n) is also known as the central binomial coefficient, and satisfies binom(2n)(n) = \frac{4n-2}{n} binom(2(n-1))(n-1).

# Write f(n) = binom(2n)(n) \Rightarrow f(n) = \frac{4n-2}{n} f(n-1), with f(1) = 2.


def f(m):
    x = 1
    for i in range(m):
        x = int(((4*i + 2)*x)/(i + 1))

    return x

print(f(n))

