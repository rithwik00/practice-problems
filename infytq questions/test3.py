s = 'wjlwcwhlwhfwfiugdldgdjcbxlwYCG'
s = s.lower()
answer = ''
length = 0

for i in s:
    if i in answer:
        if len(answer) > length:
            length = len(answer)
            final = answer
            answer = i
    else:
        answer += i

if len(answer) > len(final):
    print(answer)
else:
    print(final)