def calculate(operation, int1, int2):
    if operation == 'multiply':
        result = int1 * int2
    elif operation == 'divide':
        result = int(int1 / int2)
    elif operation == 'add':
        result = int1 + int2
    elif operation == 'subtract':
        result = int1 - int2
    return result


type_of_operation = input()
first_number = int(input())
second_number = int(input())

print(calculate(type_of_operation, first_number, second_number))

# operator, dictionary
import operator

def calculations(number_a, number_b, operation):
    operations_dict = {'multiply': operator.mul, 'divide': operator.truediv, \
        'add': operator.add, 'subtract': operator.sub}
    return int(operations_dict[operation](number_a, number_b))

type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculations(first_number, second_number, type_of_operation))
