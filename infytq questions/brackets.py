# check if brackets are nested properly

brackets = input()

stack = []
b = {')':'(', ']':'[', '}':'{'}
flag = False

for i in range(len(brackets)):
    if brackets[i] == '(' or  brackets[i] == '{' or brackets[i] == '[':
        stack.append(brackets[i])
        continue


    if brackets[i] == ')' or brackets[i] == ']' or brackets[i] == '}':
        if len(stack) !=0 and stack.pop() == b[brackets[i]]:            
            continue
        else:
            print(i + 1)
            flag = True
            break

if not(flag):
    print(0)