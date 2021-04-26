s = input()

maxx = 0
temp = ''
answer = ''

for i in s:
    if i not in temp:
        temp += i
    else:
        if len(temp) > 3 and maxx < len(temp):
            answer = temp
            maxx = len(temp)
        temp = i


if len(temp) > 3 and maxx < len(temp):
    answer = temp

if answer == '' or temp == '':
    print(-1)
else:
    print(answer)