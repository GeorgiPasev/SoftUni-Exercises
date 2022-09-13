string = input()

while True:
    command = input().split()
    current_command = command[0]

    if current_command == 'End':
        break

    elif current_command == 'Translate':
        char = command[1]
        replacement = command[2]
        string = string.replace(char, replacement)
        print(string)
    elif current_command == 'Includes':
        substring = command[1]
        if substring in string:
            print(True)
        else:
            print(False)
    elif current_command == 'Start':
        substring = command[1]
        if string.startswith(substring):
            print(True)
        else:
            print(False)
    elif current_command == 'Lowercase':
        string = string.lower()
        print(string)
    elif current_command == 'FindIndex':
        searched_index = command[1]
        list_of_indecies = []
        for index, char in enumerate(string):
            if searched_index == char:
                list_of_indecies.append(index)
        print(list_of_indecies[-1])
    elif current_command == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        string = ''.join([string[i] for i in range(len(string)) if i < start_index or i >= start_index + count])
        print(string)

