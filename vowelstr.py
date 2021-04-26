instr = input()

vowels = {'a', 'e', 'i', 'o', 'u'}
out_str = ''
flag = True

for i in range(len(instr)):

    if instr[i] in vowels:
        flag = False
        res = 0
        for j in range(1, i * 5 + 1, 2):
            res += j

        while res > 9:
            outnum = 0
            digits = str(res)
            for digit in digits:
                outnum += int(digit)
            res = outnum

        out_str += str(outnum)

    else:
        out_str += instr[i]

if flag:
    print(-1)
else:
    print(new_str)