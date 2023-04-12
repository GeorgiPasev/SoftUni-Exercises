from collections import deque

time = deque(map(int, input().split()))
tasks = [int(x) for x in input().split()]

Darth_Vader_Ducky = 0
Thor_Ducky = 0
Big_Blue_Rubber_Ducky = 0
Small_Yellow_Rubber_Ducky = 0

while tasks and time:
    current_time = time.popleft()
    current_task = tasks.pop()
    calculation = current_time * current_task
    if 0 <= calculation <= 60:
        Darth_Vader_Ducky += 1
    elif 60 < calculation <= 120:
        Thor_Ducky += 1
    elif 120 < calculation <= 180:
        Big_Blue_Rubber_Ducky += 1
    elif 180 < calculation <= 240:
        Small_Yellow_Rubber_Ducky += 1
    else:
        tasks.append(current_task - 2)
        time.append(current_time)

if not tasks:
    print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded: ")

    print(f"Darth Vader Ducky: {Darth_Vader_Ducky}")
    print(f"Thor Ducky: {Thor_Ducky}")
    print(f"Big Blue Rubber Ducky: {Big_Blue_Rubber_Ducky}")
    print(f"Small Yellow Rubber Ducky: {Small_Yellow_Rubber_Ducky}")
    