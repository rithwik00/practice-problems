from sys import stdin, stdout
f = open('input.txt', 'r')
stdin = f
input = stdin.readline

##########################################################
# your code goes here.
def ifindex(row,  col, p, q):
        
    if row < p and col < q:
        return True
    else:
        return False

n = int(input())
p = int(input())

matrix1 = []
matrix2 = []

for _ in range(n):
    matrix1.append(list(map(int, input().split())))


for _ in range(p):
    matrix2.append(list(map(int, input().split())))

q = len(matrix2[0])
m = len(matrix1[0])

outmatrix = []

for row in range(n): 
    for col in range(m):
        temp = {}
        l = [[row, col], [col, row], [row, row], [col, col]]

        for i in l:
            if ifindex(i[0], i[1], p, q):
                if matrix2[i[0]][i[1]] in temp:
                    temp[matrix1[row][col] * matrix2[i[0]][i[1]]] += 1
                else:
                    temp[matrix1[row][col] * matrix2[i[0]][i[1]]] = 1
            
        if len(temp) == 0:
            matrix1[row][col] = -1
            continue

        maxx = 0
        mkey = []
       
        for key in temp:
            if temp[key] >= maxx:
                maxx = temp[key]
                mkey.append(key)
        
        matrix1[row][col] = min(mkey)
       

for i in matrix1:
    print(*i)

##########################################################
f.close()