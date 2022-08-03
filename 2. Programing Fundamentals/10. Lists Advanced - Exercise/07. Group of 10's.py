numbers = list(map(int, input().split(", ")))

boundary = 0
group = []

while list(set(numbers)) != [0]:
    boundary += 10

    for number in range(len(numbers)):
        if boundary - 10 < numbers[number] <= boundary:
            group.append(numbers[number])
            numbers[number] = 0
    print(f"Group of {boundary}'s: {group}")
    group = []