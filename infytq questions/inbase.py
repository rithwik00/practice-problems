innum = int(input())
inbase = int(input())

max_zeoes = 0
count = 0

while(innum >= inbase):

    if innum % inbase == 0:
        count += 1
    else:
        if count > max_zeoes:
            max_zeoes = count
        count = 0

    innum = innum // inbase

print(max(count, max_zeoes))