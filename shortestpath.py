'''
You are given a square grid with some cells open (.) and some blocked (X). 
Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell.
Given a grid, a start and a goal, determine the minmum number of moves to get to the goal.

Example.

The grid is shown below:

...
.X.
...
The starting position  so start in the top left corner. The goal is . The path is . It takes  moves to reach the goal.

Function Description
Complete the minimumMoves function in the editor.

minimumMoves has the following parameter(s):

string grid[n]: an array of strings that represent the rows of the grid
int startX: starting X coordinate
int startY: starting Y coordinate
int goalX: ending X coordinate
int goalY: ending Y coordinate
Returns

int: the minimum moves to reach the goal
Input Format

The first line contains an integer , the size of the array grid.
Each of the next  lines contains a string of length .
The last line contains four space-separated integers, 

'''

def isValid(x, y):
    if (x, y) not in visited and x >=0 and x < rows and y >= 0 and y < cols and grid[x][y] == '.':
        return True
    return False

########################################################################
def countWays(row, col):
    size = 0
    queue = []
    visited.add((row, col)) 
    queue.append([row, col])
    
    while len(queue) > 0:
        x, y = queue.pop(0)
        if x == goalX and y == goalY:
            return size
        size += 1
        for p in pairs:
            xx = x + p[0]
            yy = y + p[1]
            
            if isValid(xx, yy) and grid[xx][yy] == '.':
                visited.add((xx, yy)) 
                queue.append([xx, yy])
                
    return size
########################################################################
rows = int(input())
grid = []

pairs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

for i in range(rows):
    grid.append(input())
    
startX, startY, goalX, goalY = map(int, input().split())
cols = len(grid[0])
########################################################################
visited = set()
count = countWays(startX, startY)
if count % 2 == 0:
    print(count // 2)
else:
    print(count // 2 + 1)
