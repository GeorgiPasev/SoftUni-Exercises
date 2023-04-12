size = int(input())
directions = input().split(', ')
matrix = [list(input()) for _ in range(size)]
hazelnuts = 0
squirrel_row = 0
squirrel_col = 0
collected = False
trap = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            squirrel_row = row
            squirrel_col = col
            break
    

for direction in directions:
    if direction == 'left':
        squirrel_col -= 1
        if squirrel_row < 0 or squirrel_row >= size or squirrel_col < 0 or squirrel_col >= size:
            break
        if matrix[squirrel_row][squirrel_col] == 'h':
            hazelnuts += 1
            matrix[squirrel_row][squirrel_col] = '*'
        elif matrix[squirrel_row][squirrel_col] == 't':
            trap = True
            break
    elif direction == 'right':
        squirrel_col += 1
        if squirrel_row < 0 or squirrel_row >= size or squirrel_col < 0 or squirrel_col >= size:
            break
        if matrix[squirrel_row][squirrel_col] == 'h':
            hazelnuts += 1
            matrix[squirrel_row][squirrel_col] = '*'
        elif matrix[squirrel_row][squirrel_col] == 't':
            trap = True
            break
    elif direction == 'up':
        squirrel_row -= 1
        if squirrel_row < 0 or squirrel_row >= size or squirrel_col < 0 or squirrel_col >= size:
            break
        if matrix[squirrel_row][squirrel_col] == 'h':
            hazelnuts += 1
            matrix[squirrel_row][squirrel_col] = '*'
        elif matrix[squirrel_row][squirrel_col] == 't':
            trap = True
            break
    elif direction == 'down':
        squirrel_row += 1
        if squirrel_row < 0 or squirrel_row >= size or squirrel_col < 0 or squirrel_col >= size:
            break
        if matrix[squirrel_row][squirrel_col] == 'h':
            hazelnuts += 1
            matrix[squirrel_row][squirrel_col] = '*'
        elif matrix[squirrel_row][squirrel_col] == 't':
            trap = True
            break
    if hazelnuts == 3:
        collected = True
        break


if collected:
    print(f"Good job! You have collected all hazelnuts!")
else:
    if trap:
        print(f"Unfortunately, the squirrel stepped on a trap...")
    elif squirrel_row < 0 or squirrel_row >= size or squirrel_col < 0 or squirrel_col >= size:
        print(f"The squirrel is out of the field.")
    else:
        print(f"There are more hazelnuts to collect.")
    
print(f"Hazelnuts collected: {hazelnuts}")