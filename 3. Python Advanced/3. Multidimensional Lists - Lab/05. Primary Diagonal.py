N = int(input())
matrix = []

for _ in range(N):
    matrix.append([int(x) for x in input().split()])

diagonal = 0
for idx in range(N):
    diagonal += matrix[idx][idx]

print(diagonal)