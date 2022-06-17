width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
boxes_finished = False
cubic_meters_free_space = width_free_space * length_free_space * height_free_space

while cubic_meters_free_space > 0:
    command = input()
    if command == "Done":
        boxes_finished = True
        break
    cubic_meters_free_space -= int(command)

if boxes_finished:
    print(f"{cubic_meters_free_space} Cubic meters left.")
else:
    cubic_meters_free_space = abs(cubic_meters_free_space)
    print(f"No more free space! You need {abs(cubic_meters_free_space)} Cubic meters more.")
    