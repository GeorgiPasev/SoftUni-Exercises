def is_perfect(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
    if number == sum_of_divisors:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))