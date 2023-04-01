N = int(input())
matrix = [list(input()) for _ in range(N)]

find = input()
found = False
for row in range(N):
    for col in range(N):
        if matrix[row][col] == find:
            print(f'({row}, {col})')
            found = True
            break
    if found:
        break

if not found:
    print(f'{find} does not occur in the matrix')