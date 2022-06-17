n = int(input())
sum_left = 0
sum_right = 0

for number in range(1, n + 1):
    value = int(input())
    sum_left += value
for number in range(1, n + 1):
    value = int(input())
    sum_right += value

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(f"No, diff = {diff}")

