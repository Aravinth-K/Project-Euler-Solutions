x = []

# We scan over i and j such that i < j < 100 - i - j. We then store these results in x.
for i in range(1,332):
    for j in range(i+1,499):
        if i < j and j < (1000 - i - j):
            x.append([i, j, 1000 - i - j])
        else:
            continue

y = []

# We test whether the tuples given in the previous loop satisfy the pythagorean triple condition, and store these in y.
for i in range(len(x)):
    (x[i][0])**2 + (x[i][1])**2 == (x[i][2])**2 and y.append(x[i])

# If there is only one solution (which there is) we print it.
if len(y) == 1:
    print(y[0][0]*y[0][1]*y[0][2])
else:
    None
