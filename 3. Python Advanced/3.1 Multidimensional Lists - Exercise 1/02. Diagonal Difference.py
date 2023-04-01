N = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(N)]
primary_diagonal = [matrix[i][i] for i in range(N)]
secondary_diagonal = [matrix[i][N - i - 1] for i in range(N)]

differece = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(differece)