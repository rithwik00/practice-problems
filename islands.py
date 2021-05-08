# count the number of  distinct islands

from sys import stdin, stdout

f = open('input.txt', 'r')
stdin = f
input = stdin.readline
# dfs method
##########################################################

# check if the location is valid
def isSafe(row, col):
    if row >= 0 and row < ROWS and col >= 0 and col < COLS and island_matrix[row][col] == 1 and (row, col) not in visited:
        return True
    else:
        return False

# main function
def count_adj_ones(row, col):
    # all the adjacent row and col locations in row and col array
    rowN = [-1, -1, -1, 0, 0, 1, 1, 1]
    colN = [-1, 0, 1, -1, 1, -1, 0, 1]

    # mark the location as visited
    visited.add((row, col))
    
    # check for adjacent locations
    for k in range(0, 8):
        xx = row + rowN[k]
        yy = col + colN[k]
        if isSafe(xx, yy):
            count_adj_ones(xx, yy)

# 1s denote the island
# 0s denote water 
island_matrix =[[1, 0, 0, 1],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 1, 1]]

visited = set()
count  = 0

ROWS = len(island_matrix)
COLS = len(island_matrix[0])

for row in range(ROWS):
    for element in range(COLS):
        if island_matrix[row][element] == 1 and (row, element) not in visited: 
            count_adj_ones(row, element)
            count += 1

print(count)
##########################################################

f.close()