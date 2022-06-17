command = input()
voldemort = False

while command != "Welcome!":
    if command == "Voldemort":
        voldemort = True
        break
    legth_of_name = len(command)
    if legth_of_name < 5:
        print(f"{command} goes to Gryffindor.")
    elif legth_of_name == 5:
        print(f"{command} goes to Slytherin.")
    elif legth_of_name == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")
    if command == "Black":
        print(f"{name} goes to Azkaban")
    command = input()

if voldemort:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
