eggs_player_one = int(input())
eggs_player_two = int(input())
end = False

while eggs_player_one != 0 and eggs_player_two != 0:
    command = input()
    if command == "End of battle":
        end = True
        break
    if command == "one":
        eggs_player_two -= 1
    elif command == "two":
        eggs_player_one -= 1

if end:
    print(f"Player one has {eggs_player_one} eggs left.")
    print(f"Player two has {eggs_player_two} eggs left.")
elif eggs_player_one == 0:
    print(f"Player one is out of eggs. Player two has {eggs_player_two} eggs left.")
elif eggs_player_two == 0:
    print(f"Player two is out of eggs. Player one has {eggs_player_one} eggs left.")