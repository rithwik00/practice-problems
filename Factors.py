import math
# import pandas

def factors(num):
    i = 1

    while i <= math.sqrt(num):

        if num % i == 0:
            if num // i == i:
                print(i, end = ' ')
            else:
                print(i, num // i, end = ' ')
                # print(num // i)

        i += 1

factors(100)