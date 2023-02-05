from collections import deque

water_quantity = int(input())
water_queue = deque([])
    
while True:
    command = input()
    if command == "Start":
        break
    water_queue.append(command)

while True:
    command = input()
    if command == "End":
        break
    command_args = command.split()
    if len(command_args) == 2:
        water_quantity += int(command_args[1]) #refill
    else:
        liters_for_person = int(command_args[0])
        person_name = water_queue.popleft()
        if liters_for_person > water_quantity:
            print(f"{person_name} must wait")
        else:
            print(f"{person_name} got water")
            water_quantity -= liters_for_person

print(f"{water_quantity} liters left")