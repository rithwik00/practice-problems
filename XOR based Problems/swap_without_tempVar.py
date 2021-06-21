'''
Given two variables, x, and y, 
swap two variables without using a third variable.
'''

x = 10
y = 5

x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)