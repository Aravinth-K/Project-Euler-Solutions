# We start with a dictionary containing the numbers 1 to 19 and their associated spellings.
dict = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}

# tens adds the numbers 20 to 99 to dict. It takes in a given preposition, given below by tenList, adds 'teen', and takes in a number which will form the key in the dictionary.
def tens(word, n):
    dict[n] = word
    for i in range(n + 1, n + 10):
        dict[i] = word + dict[i-n]

tenList = ['twen', 'thir', 'for', 'fif'] + [dict[i] for i in range(6,10)]

for i in range(0, 8):
    tens(tenList[i]+'ty', (i+2)*10)

# Similarly, hundreds adds the numbers 100 to 999.
def hundreds(n):
    i = 100 * n
    dict[i] = dict[n] + 'hundred'
    for j in range(i+1,i+100):
        dict[j] = dict[i] + 'and' + dict[j - i] 

for i in range(1,10):
    hundreds(i)

# We manually add 1000 to dict.
dict[1000] = dict[1] + 'thousand'

# We list all of the words associated to each number from 1 to 1000.
words = list(dict.values())

count = 0

# We add up the number of letters in all the words.
for x in words:
    s = 0
    for i in x:
        s += 1
    count += s

print(count)





