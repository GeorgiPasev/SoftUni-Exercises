from sys import maxsize

rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
biggest_square = []
biggest_square_sum = -maxsize

for row in range(rows - 2):
    for col in range(cols - 2):
        square = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]
        square_sum = sum(sum(square, []))
        if square_sum > biggest_square_sum:
            biggest_square_sum = square_sum
            biggest_square = square

print(f"Sum = {biggest_square_sum}")
[print(' '.join(map(str, row))) for row in biggest_square]