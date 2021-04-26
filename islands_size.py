from sys import stdin, stdout
f = open('input.txt', 'r')
stdin = f
input = stdin.readline

# BFS method
##########################################################

def isValid(row, col):
    return row < rows and row >= 0 and col < cols and col >= 0
    
def land_count(row, col):
    size = 0 # counts number of continuous 1s 
    queue = []
    Map[row][col] = 0 # marking visited island as 0
    queue.append([row, col])
    
    while len(queue) > 0:
        x, y = queue.pop(0)
        size += 1
        for p in pairs:
            xx = x + p[0]
            yy = y + p[1]
            if isValid(xx, yy) and Map[xx][yy] == 1:
                Map[xx][yy] = 0
                queue.append([xx, yy])

    return size


rows, m = map(int, input().split())
Map = []
pairs = [[-1, 0], [0, -1], [1, 0], [0, 1]] # checks all four directions
land_size = []

for _ in range(rows):
    Map.append(list(map(int, input().split())))

cols = len(Map[0])

for row in range(rows):
    for col in range(cols):
        if isValid(row, col) and Map[row][col] == 1:
            count = land_count(row, col)
            land_size.append(count)

print(land_size) # prints sizes of the islands

##########################################################

f.close()