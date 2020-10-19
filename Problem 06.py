print("Input the number you want to go up to.")

n = int(input("> "))

# Works out the sum of the squares.
x = []

for i in range(n+1):
    x.append(i*i)

# Work out the sum.
y = []

for i in range(n+1):
    y.append(i)

# Compute the difference between the square of the sum and the sum of the squares.
z = sum(y)*sum(y) - sum(x)

print(f"The difference is {z}.")
