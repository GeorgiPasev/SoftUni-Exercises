goal_lv = int(input())
current_money = 0
closed = False

while current_money < goal_lv:
    command = input()
    if command == "closed":
        closed = True
        break
    elif command == "haircut":
        command_2 = input()
        if command_2 == "mens":
            current_money += 15
        elif command_2 == "ladies":
            current_money += 20
        elif command_2 == "kids":
            current_money += 10
    elif command == "color":
        command_2 = input()
        if command_2 == "touch up":
            current_money += 20
        elif command_2 == "full color":
            current_money += 30


if closed:
    diff = goal_lv - current_money
    print(f"Target not reached! You need {diff}lv. more.")
else:
    print("You have reached your target for the day!" )

print(f"Earned money: {current_money}lv.")