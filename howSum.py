# takes targetSum and array of numbers as input
# return array of any combination of elements that add up to the targetsum

def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        result = howSum(remainder, numbers)

        if result != None:
            return result + [num]

    return None

print(howSum(7, [2,4])) 