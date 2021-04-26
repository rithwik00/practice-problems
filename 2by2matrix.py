def check(matrix):
    for i in matrix:
        for j in i:
            sum = 0
            for k in str(j):
                sum += int(k)
            if j % sum != 0:
                return False
    return True

rows = int( input() )

big_matrix = [[42, 54, 2],
          [30, 24, 27],
          [180, 190, 40],
          [11, 121, 13]]

# for i in range(rows):
#     big_matrix.append( list( map( int, stdin.readline().split() ) ) )
#big_matrix = np.array(big_matrix)
cols = len(big_matrix[0])

matching_shape = (2, 2) #rows, cols

pointer = [0, 0]

for i in range(rows - matching_shape[0] + 1):
    for j in range(cols - matching_shape[1] + 1):
        pointer = [i, j]
        #print(pointer)
        #tmp = big_matrix[ i:i + matching_shape[0], j:j + matching_shape[1] ]
        tmp = [k[j:j + matching_shape[1]] for k in big_matrix[i:i + matching_shape[0]]]
        #print(tmp)
        flag = check( tmp )
        if flag:
            for ii in tmp:
                print(*ii)