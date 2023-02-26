numbers = tuple(map(float, input().split()))

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

for number in unique:
    number_count = numbers.count(number)
    print(f"{number} - {number_count} times")

#alt
numbers = tuple(map(float, input().split()))
unique = []
output = {}

for number in numbers:
    if number not in unique:
        unique.append(number)

for number in unique:
    number_count = numbers.count(number)
    output[number] = str(f"{number_count} times")

for key, value in output.items():
    print(f"{key} - {value}")

#alt
numbers = tuple(map(float, input().split()))

nums_and_occurances = {}
for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]

#alt

from collections import Counter
 
nums = input().split(' ')
 
counter = Counter(nums)
 
for num, count in counter.items():
    print(f"{float(num):.1f} - {count} times")