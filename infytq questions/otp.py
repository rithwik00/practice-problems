number = input()
answer = ''
for i in range(1, len(number), 2):
    answer += str(int(number[i]) ** 2)

    if len(answer) > 4:
        break

print(answer[:4])
    