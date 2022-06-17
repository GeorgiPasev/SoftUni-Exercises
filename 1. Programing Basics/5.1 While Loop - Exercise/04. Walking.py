steps_walked_input = input()
sum_steps_walked = 0
goal_reached = False

while steps_walked_input != "Going home":
    steps_walked_input = int(steps_walked_input)
    sum_steps_walked += steps_walked_input
    if sum_steps_walked >= 10000:
        goal_reached = True
        break
    steps_walked_input = input()
else:
    steps_walked_input = int(input())
    sum_steps_walked += steps_walked_input
    if sum_steps_walked >= 10000:
        goal_reached = True



diff = abs(sum_steps_walked - 10000)
if goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")