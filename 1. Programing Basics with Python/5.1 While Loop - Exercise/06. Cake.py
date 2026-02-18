width_cake = int(input())
length_cake = int(input())
total_cake_slices = width_cake * length_cake
no_more_cake = False

command = input()
while command != "STOP":
    total_cake_slices -= int(command)
    if total_cake_slices <= 0:
        no_more_cake = True
        break
    command = input()

if no_more_cake:
    print(f"No more cake left! You need {abs(total_cake_slices)} pieces more.")
else:
    print(f"{total_cake_slices} pieces are left.")