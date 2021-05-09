# takes targetSum and array of numbers as input
# return array of any combination of elements(repeated allowed) that add up to the targetsum

def howSum(targetSum, numbers):
    if targetSum in visited:
        return visited[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        result = howSum(remainder, numbers)

        if result != None:
            visited[targetSum] = result + [num]
            return visited[targetSum]

    visited[targetSum] = None
    return None

visited = {}
print(howSum(300, [2,4])) 