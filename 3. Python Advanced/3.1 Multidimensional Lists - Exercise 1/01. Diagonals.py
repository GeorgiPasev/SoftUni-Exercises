rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary_diagonal, secondary_diagonal = [], []

for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - idx - 1])
    # could also make it [idx - 2*idx] to get the same result (have to start from 1, idx+1)

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
