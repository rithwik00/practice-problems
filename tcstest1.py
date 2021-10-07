# 1, 2 and 5
coins = [5, 2, 1]
n = 13

one = 0
two = 0
five = (n - 4) // 5

if (n - 5 * five) % 2 == 0:
    one = 2
else:
    one = 1

two = (n - 5 * five - one) // 2

print(five, two, one)