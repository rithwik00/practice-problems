from sys import stdin, stdout
f = open('input.txt', 'r')
stdin = f
input = stdin.readline

##########################################################
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
##########################################################
class Node:

    def __init__(self, pt, dist):
        self.pt = pt
        self.dist = dist

##########################################################
def BFS(maze, source, destination):
    queue = []
    visited = set()
    

ROWS = int(input())
COLS = int(input())
source = (0, 0)
destination = (3, 0)
maze = []

for i in range(m):
    maze.append(list(map(int, input().split())))

print(BFS(maze, source, destination))
##########################################################

f.close()

'''
input:

4
4
0 * 0 s
* 0 * *
0 * * *
d * * *

s => source
d => destination
* => safe cell
0 => unsafe cell
'''