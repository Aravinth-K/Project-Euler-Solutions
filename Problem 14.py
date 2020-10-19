# The iteration function gives the Collatz sequence. It takes the last number and outputs the next one.
def iteration(n):
    if n % 2 ==0:
        n = int(n/2)
    else:
        n = 3*n + 1
    return n

# max_value takes an input list and outputs the largest value out of the first element of each sublist.
def max_value(inputlist):
    return max([sublist[0] for sublist in inputlist])

# Input the limit of Collatz numbers.
limit = int(input("> "))

# Initialise a dictionary contianing Collatz sequence length and associated starting number.
seq = {}

for i in range(limit):
    num = i + 1
    count = 1
    # Implement the Collatz sequence until we reach 1.
    while num != 1:
        # If the number the last cycle generates is already in the dictionary of seq, we just output that count + that value.
        if seq.get(num,0) != 0:
            count += seq[num] - 1
            break
        else:
            count += 1
            num = iteration(num)
    seq[i+1] = count

# Calculate the longest Collatz sequence values.
max_value = max(seq.values())

# Find the associated keys in the seq, giving the starting numbers.
max_keys = [k for k, v in seq.items() if v == max_value]

print(f" The numbers with the longest chain is {max_keys} of length {max_value}")
