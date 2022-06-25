def is_even(a):
    if int(a) % 2 == 0:
        return True


numbers = input().split()
filtered_numbers = []
for number in numbers:
    if is_even(number):
        filtered_numbers.append(int(number))

print(filtered_numbers)


# lambda, list comprehension
numbers_as_digits = [int(s) for s in input().split()]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


# shortest possible but not readable
numbers_as_digits = [int(s) for s in input().split() if int(s)%2==0]
print(numbers_as_digits)
