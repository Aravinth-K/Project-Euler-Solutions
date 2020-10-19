# This dictionary assigns numbers 1 to 12 for Jan - Dec, and gives the number of days in each as values.
month_n = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

# This is the corresponding leap year dictionary.
month_l = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

# count gives the number of months starting on a Sunday.
count = 0

# We start with the year 1901.
year = 1901

# 1901 starts on a Tuesday, which is given number 2.
day = 2

# We can work out the starting day of each month by taking the previous first day number and adding the numbers of days in each month modulo 7. Each if elif elif else clause identifies whether the correspodning year is a leap year or not.
while year < 2001:
    if (((year % 100) == 0) & ((year % 400) == 0)):
        for i in range(1,13):
            if day == 0:
                count += 1
            else:
                None
            day += month_l[i]
            day = day % 7
    elif (((year % 100) == 0) & ((year % 400) != 0)):
        for i in range(1,13):
            if day == 0:
                count += 1
            else:
                None
            day += month_n[i]
            day = day % 7
    elif (year % 4) == 0:
        for i in range(1,13):
            if day == 0:
                count += 1
            else:
                None
            day += month_l[i]
            day = day % 7
    else:
        for i in range(1,13):
            if day == 0:
                count += 1
            else:
                None
            day += month_n[i]
            day = day % 7
    year += 1

print(count)

print(day)


