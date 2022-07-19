wagons = [0] * int(input()) #train = [0 for wagon in range(int(input()))]

command = input()

while command != "End":
    data = command.split()
    current_command = data[0]
    if current_command == 'add':
        people_to_add = int(data[1])
        wagons[-1] += people_to_add
    elif current_command == 'insert':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people
    elif current_command == 'leave':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people
    
    command = input()

print(wagons)