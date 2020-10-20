# Takes the list and two positions and swaps the values.
def swap_positions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

# Takes the list and the start and end positions of the sub-list and returns the list with the sub-list reversed.
def reverse_sublist(list,start,end):

    list[start:end] = list[start:end][::-1]
    return list

# Computes the next word in the lexicographic sequence.
def iteration(list):
    # First find the largest non-decreasing position.
    x = []
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            x.append(i)
    start = max(x)
    # We find the furthest right position of an object greater than list(start)
    y = []
    for j in range(1,len(list)):
        if list[j] > list[start] and j >= start:
            y.append(j)
    successor = max(y)
    # We swap and position start and successor and then reverse the list to generate the next list.
    list = swap_positions(list, start, successor)
    list = reverse_sublist(list, start+1, len(list) + 1)
    return list

i = 967681

# We don't need to start with the 1st element. The first 9! elements start with a 0, the next 9! start with a 1, and the next 8! start with 2 0, going on until we reach the (2*9! + 6*8!)+1th = 967681th number which starts with 2 7 0 1 3 4 5 6 8 9

list = [2,7,0,1,3,4,5,6,8,9]

while i< 1000000:
    list = iteration(list)
    i += 1

print(list)



