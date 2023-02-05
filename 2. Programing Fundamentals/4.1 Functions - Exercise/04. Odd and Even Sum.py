def sum_even_odd_digits(a):
    sum_even = 0
    sum_odd = 0
    for digit in str(a):
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    string = f"Odd sum = {sum_odd}, Even sum = {sum_even}"
    return string


single_number = int(input())

print(sum_even_odd_digits(single_number))