set_1, set_2 = {*input().split()}, {*input().split()}
N = int(input())

for i in range(N):
    command = input()
    numbers = command.split()[2:]
    if "Add First" in command:
        set_1 = set_1.union(numbers)
    elif 'Add Second' in command:
        set_2 = set_2.union(numbers)
    elif 'Remove First' in command:
        set_1 = set_1.difference(numbers)
    elif 'Remove Second' in command:
        set_2 = set_2.difference(numbers)
    else:
        print(set_1.issubset(set_2) or set_2.issubset(set_1))
        # print('True' if set_1.issubset(set_2) or set_2.issubset(set_1) else 'False')

print(*sorted(map(int, set_1)), sep=", ")
print(*sorted(map(int, set_2)), sep=", ")


