# from sys import stdin
# ans = [0]

# def generate(length, string, limit):
#     global ans
#     #print(length, string)
#     if len(string) != length:
#         ans.append(int(string))
#     if len(string) == length:
#         if(int(string) <= limit):
#             ans.append(int(string))
#         return
#     else:
#         if( int(string[-1]) != 0 ):
#             tmp = string + str( int(string[-1]) - 1 )
#             generate(length, tmp, limit)

#         if( int(string[-1]) != 9 ):
#             tmp = string + str( int(string[-1]) + 1 )
#             generate(length, tmp, limit)


# dig = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# n = int(stdin.readline())

# length = len(str(n))

# first_element = '1'

# limit = n
# for i in dig[1:]:
#     first_element = str(i)
#     generate(length, first_element, limit)
# print(*sorted(ans))


n = int(input())

def check(number):
    # print(number)
    if len(number) == 1:
        return True
    else:
        for i in range(len(number) - 1):
            if abs(int(number[i]) - int(number[i + 1])) == 1:
                continue
            else:
                return False
        return True
l = []
for i in range(n):
    if check(str(i)):
        l.append(i)
print(l)