# given cost array of length 2n, each element consists of cost of flying ith employee to cityA and cityB 
# 2n employees
# Find minimum cost such that each city contains n employees
from sys import stdin, stdout
f = open('input.txt', 'r')
stdin = f
input = stdin.readline

##########################################################
# your code goes here.
cost = [[10, 20], [30, 200], [100, 50], [30, 20]]
changed_cost = []
n = 2

for i in cost:
    changed_cost.append([i[0] - i[1], i])

changed_cost.sort()
# print(changed_cost)
cost1 = 0
for i in range(n):
    # print(changed_cost[i], changed_cost[i][1][0], changed_cost[n + i][1][0], changed_cost[n + i])
    cost1 += changed_cost[i][1][0]
    cost1 += changed_cost[n + i][1][1]

print(cost1)
##########################################################

f.close()

