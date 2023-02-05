def create_dataframe(zoo_animals, area_dict):
    while True:
        command = input().split(": ")
        current_command = command[0]
        if current_command == "EndDay":
            for animal in zoo_animals:
                area = zoo_animals[animal][1]
                if area not in area_dict:
                    area_dict[area] = 1
                else:
                    if zoo_animals[animal][0] > 0:
                        area_dict[area] += 1

            break

        if current_command == "Add":
            data = command[1].split("-")
            animal_name = data[0]
            needed_food_quantity = int(data[1])
            area = data[2]
            if animal_name not in zoo_animals:
                # index 0 food quantity
                # index 1 area
                # index 2 count of hungry animals
                zoo_animals[animal_name] = [needed_food_quantity, area, 0]
            else:
                zoo_animals[animal_name][0] += needed_food_quantity

        elif current_command == "Feed":
            data = command[1].split("-")
            animal_name = data[0]
            food = int(data[1])
            if animal_name in zoo_animals:
                zoo_animals[animal_name][0] -= food
            else:
                continue

            if zoo_animals[animal_name][0] <= 0:
                del zoo_animals[animal_name]
                print(f'{animal_name} was successfully fed')


def print_animals(zoo_animals, area_dict):
    print("Animals:")
    for animal_name, value in zoo_animals.items():
        food = value[0]
        print(f"{animal_name} -> {food}g")

    print("Areas with hungry animals:")
    for area, value in area_dict.items():
        print(f"{area}: {value}")


def wild_zoo():  # this is the main function
    zoo_animals = {}
    area_dict = {}
    create_dataframe(zoo_animals, area_dict)
    print_animals(zoo_animals, area_dict)


wild_zoo()