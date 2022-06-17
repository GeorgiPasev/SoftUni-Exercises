import sys
count_of_numbers = int(input())
sum = 0
max_element = -sys.maxsize

for number in range(1, count_of_numbers + 1):
    current_number = int(input())
    sum += current_number
    if current_number > max_element:
        max_element = current_number

if max_element == sum - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    difference = abs(max_element - (sum - max_element))
    print("No")
    print(f"Diff = {difference}")

# import sys
# count_of_numbers = int(input())
# sum = 0
# max_element = "" <---

# for number in range(1, count_of_numbers + 1):
#     current_number = int(input())
#     if i == 0: <---
#       max_number = current_number <---
#     sum += current_number
#     if current_number > max_element:
#         max_element = current_number

# if max_element == sum - max_element:
#     print("Yes")
#     print(f"Sum = {max_element}")
# else:
#     difference = abs(max_element - (sum - max_element))
#     print("No")
#     print(f"Diff = {difference}")
    
