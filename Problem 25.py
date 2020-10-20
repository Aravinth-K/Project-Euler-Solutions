# This problem is about memoisation, noting the output of calculations as you go to avoid multiple iterations of a function that increases run time.

fibonacci_cache = {}

def fibonacci_memo(input_value):
    if input_value in fibonacci_cache:
        return fibonacci_cache[input_value]
    if input_value == 1:
            value = 1
    elif input_value == 2:
            value = 1
    elif input_value > 2:           
            value =  fibonacci_memo(input_value -1) + fibonacci_memo(input_value -2)
    fibonacci_cache[input_value] = value
    return value

i = 0

num_digits = 0

# We scan over numbers and calculate the number of digits with num_digits.
while num_digits < 1000:
    i += 1
    num_digits = 0
    x = fibonacci_memo(i)
    while x:
        num_digits += 1
        x //= 10

print(i)

