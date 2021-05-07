
# minimum = 1e18

# l = [[0, 5, 6, 1, 6],
# [1, 6, 5, 6, 3],
# [6, 1, 6, 6, 3],
# [8, 6, 1, 1, 3],
# [8, 8, 1, 1, 3],
# [9, 9, 9, 9, 9],
# [0, 6, 6, 1, 3],
# [5, 5, 6, 3],
# [1, 2, 1, 1, 9],
# [6, 6, 1, 9],
# [8, 1, 5, 1],
# [8, 6, 6, 6, 6],
# [9, 8, 1, 6, 3],
# [9, 1, 1, 3]]

# for lis in l:
#     length = len(lis)
#     for i in range(length):
#         if i < length - 3 and lis[i] < minimum and lis[i] == lis[i + 1] == lis[i + 2] == lis[i + 3]:
#             minimum = lis[i]
# if minimum == 1e18:
#     print(-1)
# else:
#     print(minimum)

from collections import Counter

def transpose(arr, m, n):
    t_arr = [[-1]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            t_arr[j][i] = arr[i][j]
    return t_arr
    
def fdiagonal(mat):
    resu = []
    lis = []
    for i in range(len(mat)-3):
        lis.append([i,0])
    for i in range(1,len(mat[0])-3):
        lis.append([0,i])
    for i in lis:
        i,j = i[0],i[1]
        l = []
        while i < len(mat) and j < len(mat[0]):
            l.append(mat[i][j])
            i += 1
            j += 1
        resu.append(l)
    return(resu)
        
def bdiagonal(mat):
    resu = []
    lis = []
    for i in range(3,len(mat[0])):
        lis.append([0,i])
    for i in range(1,len(mat)-3):
        lis.append([i,len(mat[0])-1])
    for b in lis:
        i,j = b[0],b[1]
        l = []
        while i < len(mat) and j > -1:
            l.append(mat[i][j])
            i += 1
            j -= 1
        resu.append(l)
    return(resu)

def find_pattern(cmpr, arr, m, n):
    
    outnum = []
    # cmpr = 4
    for i in arr:
        tmp = Counter(i)
        #print(tmp.most_common())
        if( tmp.most_common(1)[0][1] < cmpr ):
            outnum.append(-1)
            continue
        else:
            prev = -1
            count = 0
            for j in i:
                #print(prev, j, count)
                if( j == prev ):
                    count += 1
                    if(count >= cmpr-1):
                        outnum.append(j)
                else:
                    prev = j
                    
    return outnum    
    # logic
    
    #return sorted(list(set(outnum)))
    
m = int(input())
arr = []
for _ in range(m):
    arr.append( list( map( int, input().split() ) ) )

n = len(arr[0])

outnum_list = []
cmpr = 4
# normal
outnum_list += ( find_pattern(cmpr, arr, len(arr), len(arr[0])) )

# transpose
t_arr = transpose(arr, m, n)
outnum_list += ( find_pattern(cmpr, t_arr, len(t_arr), len(t_arr[0])) )

# normal 45degree
arr_45 = fdiagonal(arr)
outnum_list += ( find_pattern(cmpr, arr_45, len(arr_45), len(arr_45[0])) )

# transpose 45 degree
arr_135 = bdiagonal(arr)
outnum_list += ( find_pattern(cmpr, arr_135, len(arr_135), len(arr_135[0])) )

answer = -1
#print(set(outnum_list))
answers = sorted( list( set(outnum_list) ) )
length = len(answers)
#print(answers)
if(length == 0):
    answer = -1
elif(length == 1):
    answer = answers[0]
else:
    answer = answers[1]

print(answer)