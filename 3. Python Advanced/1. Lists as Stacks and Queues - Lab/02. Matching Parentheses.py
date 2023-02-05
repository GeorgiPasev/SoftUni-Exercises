expression = input()
stack = []

for index in range(len(expression)):
    char = expression[index]
    if char == '(':
        stack.append(index)
    elif char == ')':
        start_bracket = stack.pop()
        sub_expression = expression[start_bracket:index + 1]
        print(sub_expression)
