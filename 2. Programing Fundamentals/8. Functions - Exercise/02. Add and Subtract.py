def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c


def add_and_subtract(d, e, f):
    sum_of_first_and_second_integers = sum_numbers(d, e)
    result = subtract(sum_of_first_and_second_integers, f)
    return result


first_parameter = int(input())
second_parameter = int(input())
third_parameter = int(input())

print(add_and_subtract(first_parameter, second_parameter, third_parameter))