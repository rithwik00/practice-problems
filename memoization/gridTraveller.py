def gridTraveller(m, n):

    if (m, n) in visited:
        return visited[(m, n)]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    visited[(m, n)] = gridTraveller(m - 1 , n) + gridTraveller(m, n - 1)

    return visited[(m, n)]

visited = {} 

print(gridTraveller(18, 18))
