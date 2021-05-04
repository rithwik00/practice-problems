# general method takes O(2^n) time
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# memoization => faster method takes O(n)

def fib(n):
    
    if n in visited:
        return visited[n]

    if n <= 2:
        return 1;

    visited[n] = fib(n-1) + fib(n-2)
    return visited[n]
    

visited = {}
print(fib(50))
print(visited)