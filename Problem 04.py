# Takes a number n, x turns it into a string, and y reverses it. If they are equal, we have a palindrome.
def palindromeQ(n):
    x = str(n)
    y = x[::-1]
    return x == y

# This is a generator for the numbers which we use as iterator for numbers under 900.
def pairs(n):
    for i in range(n):
        for j in range(n):
            yield i, j

# Initialise list of palindromes and dictionary of integers which identifies which numbers are multiplied to form the palindrome.
palindromes = []
integers = {}

# We scan over the range of three digit numbers starting from 999 in decreasing order and scan for palindromic numbers.
for i, j in pairs(900):
    z = (999-i)*(999-j)
    if palindromeQ(z):
        palindromes.append(z)
        integers[z] = [999-i,999-j]
    else:
        continue

# We calculate the largest of the palindromic numbers.
m = max(palindromes)

print(f"The answer is {max(palindromes)} = {integers[m][0]}*{integers[m][1]}")
