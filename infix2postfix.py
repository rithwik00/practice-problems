priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, ')': 9}

def isEmpty(arr):
    if len(arr) == 0:
        return True
    else:
        return False

infix = "a+b*((c^d)-e)^(f+g*h)-i"

operator = []

postfix = ''

for element in infix:
    # checks if the element is operator
    if element in priority:
        # check if the operator list is empty
        if isEmpty(operator):
            operator.append(element)
            
        # check if bracket closes
        elif element == ')':
                # append to postfix until ( is reached
                while(not isEmpty(operator) and operator[-1] != '('):
                    postfix += operator.pop()

                if operator[-1] == '(':
                    operator.pop()
                else:
                    break

        else:
            # check if bracket opens    
            # print(priority[element], element)
            if element == '(':
                operator.append(element)


            elif priority[element] >= priority[operator[-1]]:
                operator.append(element)
                # print('came in for', element)

            else:
                while not isEmpty(operator) and priority[element] <= priority[operator[-1]]:
                    postfix += operator.pop()
                operator.append(element)
    # if element is operand
    else:
        postfix += element

while not isEmpty(operator):
    postfix += operator.pop()

print(postfix)