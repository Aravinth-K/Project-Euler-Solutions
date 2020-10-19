print("Enter the maximum number.")

# This will give the range of numbers up to which we will scan for numbers divisible by 3 and 5.
x = int(input("> "))

# Intialising the type of variable y, which will store the numbers that are divisible by 3.
y = []

for i in range(x):
    i % 3 == 0 and y.append(i)

# Takes the values in x and adds those which are also divisble by 5.
for i in range(x):
    (i % 3 != 0) & (i % 5 == 0) and y.append(i)

# New variable summing over the elements of y.
z = sum(y)

print(z)
