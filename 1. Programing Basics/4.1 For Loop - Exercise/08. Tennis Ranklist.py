tournament_number = int(input())
initial_points = int(input())
wins = 0
final_points = 0

for tournament in range(tournament_number):
    result = input()
    if result == "W":
        final_points += 2000
        wins += 1
    elif result == "F":
        final_points += 1200
    elif result == "SF":
        final_points += 720

final_points += initial_points
average_points = int((final_points - initial_points) / tournament_number)
percent_won = wins / tournament_number * 100
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")