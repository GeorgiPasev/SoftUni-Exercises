tasks = []

command = input()
while command != 'End':
    data = command.split('-')
    priority = int(data[0])
    task = data[1]
    tasks.append((priority, task))
    command = input()

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)

#alternative
notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)