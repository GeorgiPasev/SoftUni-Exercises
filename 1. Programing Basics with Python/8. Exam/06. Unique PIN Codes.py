upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())



for i in range(2, upper_limit_first_number + 1):
    if i % 2 == 1:
        continue
    for j in range(2, upper_limit_second_number + 1):
        if j == 4 or j == 6 or j == 8 or j == 9 or j == 10 or j == 12:
            continue
        for k in range(2, upper_limit_third_number + 1):
            if k % 2 == 1:
                continue
            print(f"{i} {j} {k}")



