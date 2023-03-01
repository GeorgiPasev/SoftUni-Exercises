n = int(input())
car_nums = {*()}

for i in range(n):
    direction, number = input().split(", ")
    if direction == "OUT":
        car_nums.discard(number)
    else:
        car_nums.add(number)

if car_nums:
    print(*car_nums, sep="\n")
else:
    print("Parking Lot is Empty")