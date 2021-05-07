# input => targetsum and array of numbers
# return shortest combination of numbers that add up to exactly the targetsum
# if there is a tie the shortest combination, you may return any one of the shortest

def bestSum(targetSum, numbers):
    if targetSum in visited:
        return visited[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    shortest_combo = None

    for num in numbers:
        remainder = targetSum - num
        result = bestSum(remainder, numbers)

        if result != None:
            combination = result + [num]

            if shortest_combo == None or len(combination) < len(shortest_combo):
                shortest_combo = combination

    visited[targetSum] = shortest_combo
    return shortest_combo

visited = {}
print(bestSum(100, [5, 3, 4, 7]))