number_of_lines = int(input())
capacity = 255
current_capacity = 0

for line in range(number_of_lines):
    liters_added = int(input())
    if capacity - liters_added < 0:
        print("Insufficient capacity!")
        continue
    current_capacity += liters_added
    capacity -= liters_added
print(current_capacity)

