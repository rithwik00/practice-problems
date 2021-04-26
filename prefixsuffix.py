s = input()
n = len(s)

for i in range(n // 2, 0, -1):

    prefix = s[0 : i]
    suffix = s[n - i : n]

    if prefix == suffix:
        print(prefix)
        break