# n gives the number of rows of the triangle.
n = 15

# l gives the triangle as a list of lists, with each sub-list containing the numbers of each row.
l = [[] for i in range(n)]

l[0] = [75]
l[1] = [95, 64]
l[2] = [17, 47, 82]
l[3] = [18, 35, 87, 10]
l[4] = [20, 4, 82, 47, 65]
l[5] = [19, 1, 23, 75, 3, 34]
l[6] = [88, 2, 77, 73, 7, 63, 67]
l[7] = [99, 65, 4, 28, 6, 16, 70, 92]
l[8] = [41, 41, 26, 56, 83, 40, 80, 70, 33]
l[9] = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
l[10] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
l[11] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
l[12] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
l[13] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
l[14] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

# path will contain the maximum path.
path = [[] for i in range(n)]

for j in range(n):

    path[j] = [[ l[j][i] ] for i in range(j+1)]

# Best to start from bottom to top. Starting at bottom row, we work out which path maximises the sum going from the next row up.

# Running from l[n-2][i = 0 to n - 2] check max((l[n-2][i] + l[n-1][i]), (l[n-2][i] + l[n-1][i+1])) then store (#n, max_sum[i]) for each i in #n-1. 

# Then running from l[n-3][i = 0 to n - 3], check max((l[n-3][i] + max_sum[i])(l[n-3] + max_sum[i+1])) and store (#n-1, max_sum[i])) etc.


for j in range(2, n+1):

    for i in range(n+1-j):
        l[n-j][i] = max((l[n-j][i] + l[n-j+1][i]), (l[n-j][i] + l[n-j+1][i+1]))

# We output the largest sum.
print(l[0][0])

for j in range(2, n + 1):
    for i in range(n + 1 - j):
        if (l[n-j][i] + l[n-j+1][i]) > (l[n-j][i] + l[n-j+1][i+1]):
            path[n-j][i] += path[n-j+1][i]
        else:
            path[n-j][i] += path[n-j+1][i+1]

# We output the corresponding path.
print(path[0][0])




