rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
counter = 0

# could also work with (rols - 1) and (cols - 1)

for row in range(rows):
    if row == rows - 1:
        continue
    for col in range(cols):
        if col == cols - 1:
            continue
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)