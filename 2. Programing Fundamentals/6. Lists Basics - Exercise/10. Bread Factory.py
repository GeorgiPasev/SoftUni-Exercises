working_day_events = input().split("|")
energy = 100
coins = 100
events_handled = True

for event in working_day_events:
    current_event = event.split("-")
    if "rest" in current_event:
        if energy + int(current_event[1]) > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += int(current_event[1])
            gained_energy = current_event[1]
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif "order" in current_event:
        if energy - 30 < 0:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += int(current_event[1])
            print(f"You earned {current_event[1]} coins.")
    else:
        if coins >= int(current_event[1]):
            coins -= int(current_event[1])
            print(f"You bought {current_event[0]}.")
        else:
            print(f"Closed! Cannot afford {current_event[0]}.")
            events_handled = False
            break
    
if events_handled:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
