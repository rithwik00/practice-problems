'''
Given a set of numbers where all elements occur even number of times except one number, find the odd occurring number.
'''

def findOdd(arr, n):
    res = 0
    for i in range(n):
        res ^= arr[i]

    return res

arr = [12, 12, 14, 90, 14, 14, 14]
n = len(arr)

print(findOdd(arr, n))