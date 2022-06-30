experience_needed = float(input())
count_of_battles = int(input())
total_experience = 0
collected = False
battle_count = 0

for battle in range(1, count_of_battles + 1):
    current_experience_gained = float(input())
    total_experience += current_experience_gained
    if battle % 3 == 0:
        total_experience += current_experience_gained * 0.15
    if battle % 5 == 0:
        total_experience -= current_experience_gained * 0.10
    if battle % 15 == 0:
        total_experience += current_experience_gained * 0.05
    battle_count += 1
    if total_experience >= experience_needed:
        collected = True
        break


if collected:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    more_experience_needed = abs(total_experience - experience_needed)
    print(f"Player was not able to collect the needed experience, {more_experience_needed:.2f} more needed.")
