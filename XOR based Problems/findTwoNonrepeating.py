'''
Given an array in which all numbers except two are repeated once. (i.e. we have 2n+2 numbers and n numbers are occurring twice and remaining two have occurred once). 
Find those two numbers in the most efficient way.
'''


def UniqueNumbers(arr, n):
   
  sums = 0
   
  for i in range(0, n):
    sums = (sums ^ arr[i])
     
  # Bitwise & the sum with it's 2's Complement
  # Bitwise & will give us the sum containing only the rightmost set bit
  sums = (sums & -sums)
 
  # sum1 and sum2 will contain 2 unique elements initialized with 0
  # number xored with 0 is number itself
  sum1 = 0
  sum2 = 0
 
  # Traversing the array again
  for i in range(0, len(arr)):
     
    # Bitwise & the arr[i] with the sum
    # Two possibilities either result == 0 or result > 0
    if (arr[i] & sums) > 0:
      # If result > 0 then arr[i] xored
      # with the sum1
      sum1 = (sum1 ^ arr[i])
       
    else: 
      # If result == 0 then arr[i] xored with sum2
      sum2 = (sum2 ^ arr[i])
 
  print(sum1, sum2)

if __name__ == "__main__":
   
    arr = [ 2, 3, 7, 9, 11, 2, 3, 11 ]
    n = len(arr)
     
    UniqueNumbers(arr, n)