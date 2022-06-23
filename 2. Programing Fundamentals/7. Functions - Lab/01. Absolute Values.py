# For loop, enumerate
numbers = input().split()

for index, element in enumerate(numbers):
    element = abs(float(element))
    numbers[index] = element
print(numbers)

# Append to new []
numbers = input().split()
abs_numbers = []
for num in numbers:
    abs_numbers.append(abs(float(num)))

print(abs_numbers)

# map and list comprehension
numbers = list(map(float, input().split()))
result = [abs(num) for num in numbers]
print(result)

# function, map
def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result

numbers = list(map(float, input().split()))
print(abs_numbers(numbers))