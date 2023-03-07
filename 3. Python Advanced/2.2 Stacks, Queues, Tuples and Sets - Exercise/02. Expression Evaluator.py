from functools import reduce
expression = input().split()
stack = []

for item in expression:
    if item.lstrip('-').isnumeric():
        stack.append(int(item))
    else:
        if item == '*':
            stack = [reduce(lambda a, b: a * b, stack)]
        elif item == '/':
            stack = [reduce(lambda a, b: a // b, stack)]
        elif item == '+':
            stack = [reduce(lambda a, b: a + b, stack)]
        else:
            stack = [reduce(lambda a, b: a - b, stack)]

print(stack[0])