from_number = int(input())
to_number = int(input())
magic_number = int(input())
counter_combination_number = 0
found_magic_number = False

for x1 in range(from_number, to_number + 1):
    for x2 in range(from_number, to_number + 1):
        counter_combination_number += 1
        if x1 + x2 == magic_number:
            found_magic_number = True
            break
    if found_magic_number == True:
        break

if found_magic_number:
    print(f"Combination N:{counter_combination_number} ({x1} + {x2} = {magic_number})")
else:
    print(f"{counter_combination_number} combinations - neither equals {magic_number}")