def solve(a, b, l):
    li = [a, b]
    # print('li', li)
    while (a + b) in l:
        li.append(a+b)
        temp = a
        a = b
        b = temp + b

    return li

l = [2,6,3,5,8,9]
answer = []

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] in l:
            buffer = solve(l[i], l[j], l)
            answer.append(buffer)

print(answer)