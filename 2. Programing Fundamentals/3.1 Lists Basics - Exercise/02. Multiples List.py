factor = int(input())
count = int(input())
list_of_numbers = []

for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)

print(list_of_numbers)

#Alternative but not very readable
factor = int(input())
count = int(input())

list_of_numbers = list(range(factor, count * factor + 1, factor))
print(list_of_numbers)
