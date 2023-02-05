command = ""
number_of_coffees = 0
while command.lower() != "end":
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" \
        or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            number_of_coffees += 1
        else: # elif command.isupper():
            number_of_coffees += 2
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)

#Alternative
command = input()
number_of_coffees = 0

while command != "END":
    if command == "coding":
        number_of_coffees += 1
    elif command == "cat" or command == "dog":
        number_of_coffees += 1
    elif command == "movie":
        number_of_coffees += 1
    elif command == "CODING":
        number_of_coffees += 2
    elif command == "CAT" or command == "DOG":
        number_of_coffees += 2
    elif command == "MOVIE":
        number_of_coffees += 2
    command = input()

if number_of_coffees > 5:
        print("You need extra sleep")
else:
    print(number_of_coffees)