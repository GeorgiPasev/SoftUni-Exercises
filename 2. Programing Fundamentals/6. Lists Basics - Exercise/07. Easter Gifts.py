names_of_gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()
    gift = command[1]
    if command[0] == "OutOfStock":
        for index, element in enumerate(names_of_gifts):
            if gift == element:
                names_of_gifts[index] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(names_of_gifts): # 0 <= ... for minus index
            index = int(command[2])
            names_of_gifts[index] = gift
    if command[0] == "JustInCase":
        names_of_gifts[-1] = gift

    command = input()

count_none = names_of_gifts.count("None")
for none in range(count_none):
    names_of_gifts.remove("None")

print(" ".join(names_of_gifts))