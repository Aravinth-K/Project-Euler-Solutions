# We first open the file. p022_names.txt is a single line, so readline gives the same result as read.
open_file = open('p022_names.txt', 'r')

# define a functions that takes a string and a dict
def find_replace(string, dictionary):
    # is the item in the dict?
    for item in string:
        # iterate by keys
        if item in dictionary.keys():
            # look up and replace
            string = string.replace(item, "+" + str(dictionary[item]))
    # return updated string
    return string

# Assign data to a variable.
data = open_file.read()

# We turn that data into an array of names, sorted alphabetically.
names = data.split(",")

for i in range(len(names)):
    names[i] = names[i].replace("\"", "") 

names.sort()

# We define a dictionary scoring each letter with a number.
l_score = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

# numbers gives a list of strings with the sum of each scored name.
numbers = [find_replace(names[i], l_score) for i in range(len(names))]

for i in range(len(numbers)):
    numbers[i] = numbers[i].split("+")
    numbers[i].remove('')
    numbers[i] = list(map(int, numbers[i]))

# Scores works out the score of the name times the its position in the list.
scores = [sum(numbers[i])*(i+1) for i in range(len(numbers))]

# We print the total of all the name scores in the file.
print(sum(scores))



open_file.close()




