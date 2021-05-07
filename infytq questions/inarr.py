def findMinRec(arr, i, sumCalculated, sumTotal):
 
    if (i == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)

    return min(findMinRec(arr, i - 1, sumCalculated+arr[i - 1], sumTotal), findMinRec(arr, i - 1, sumCalculated, sumTotal))
 
def findMin(arr,  n):
 
    sumTotal = sum(arr)
    return findMinRec(arr, n, 0, sumTotal)
 
# Driver code
if __name__ == "__main__":

    arr = [87,100,28,67,68,41,67,1]
    n = len(arr)
    print(findMin(arr, n))