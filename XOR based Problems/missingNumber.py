'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list.
Write an efficient code to find the missing integer.

Assume a1 ^ a2 ^ a3 ^ …^ an = a and a1 ^ a2 ^ a3 ^ …^ an-1 = b
Then a ^ b = an
'''
def getMissingno(a, n):
    x1 = a[0]
    x2 = 1

    for i in range(1, n):
        x1 ^= a[i]
        print(x1)

    for i in range(2, n + 2):
        x2 ^= i

    print(x1, x2)

    return x1 ^ x2

a = [1,2,3,5]
n = 4
print(getMissingno(a, n))