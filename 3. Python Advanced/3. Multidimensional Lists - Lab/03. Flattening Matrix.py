rows = int(input())
matrix = [[int(col) for col in input().split(', ')] for row in range(rows)]

flattened = [num for row in matrix for num in row]

print(flattened)