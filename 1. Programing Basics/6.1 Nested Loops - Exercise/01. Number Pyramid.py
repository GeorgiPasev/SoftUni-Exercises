n = int(input())
counter = 1
# k = 1
all_is_printed = False

for row in range(1, n + 1): # we have enough iterations(probably more)
    for column in range(1, row + 1):
        print(counter, end = " ")
        counter += 1
        if counter > n:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()



# while k <= n:
#     for print_how_many_numbers in range(counter):
#         print(f"{k}", end=" ")
#         k += 1
#         if k > n:
#             break
#     counter += 1
#     print()

# Alternative way:

# n = int(input())
# row = 1
# col = 0

# for i in range(1, n + 1):
#     print(i, end=' ')
#     col += 1
#     if col == row:
#         row += 1
#         col = 0
#         print()