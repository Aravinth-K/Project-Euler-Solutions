print("Enter a maximum value.")

# This gives the maximum number up to which we will compute Fibonacci numbers.
n = int(input("> "))

# We give the first two Fibonacci numbers. 
x = [1,2]

# Initialising list type for a new variable y which will store the even Fibonacci numbers.
y = []

i = 0

# Generate the Fibonacci sequence
while x[i+1] < n:
    z = x[i] + x[i+1]
    if z > n:
        break
    x.append(z)
    i += 1

# Find the even set
for i in x:
    i % 2 == 0 and y.append(i)

print(sum(y))
