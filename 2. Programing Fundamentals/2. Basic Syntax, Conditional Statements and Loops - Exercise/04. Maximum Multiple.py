divisor = int(input())
boundary = int(input())
max_multiplier = 0

for i in range(boundary, divisor, -1):
    if i % divisor == 0:
        max_multiplier = i
        break
print(max_multiplier)




# divisor = int(input())
# boundary = int(input())

# while boundary % divisor != 0:
#     boundary -= 1

# print(boundary)