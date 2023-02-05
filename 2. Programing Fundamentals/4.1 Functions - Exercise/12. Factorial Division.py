def factorial(number):
    for num in range(1, number):
        number *= num
    return number

first_number = int(input())
second_number = int(input())
division = factorial(first_number) / factorial(second_number)
print(f"{division:.2f}")
