# return true if given sum is possibleusing elements in array else false

def canSum(targetSum, numbers):
    if targetSum in visited:
        return visited[targetSum]
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers):
            visited[targetSum] = True
            return True

    visited[targetSum] = False    
    return False

visited = {}
print(canSum(300, [7, 14]))