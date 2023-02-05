from collections import deque
people = deque()

while True:
    line = input()
    if line == 'End':
        print(f"{len(people)} people remaining.")
        break

    if line == 'Paid':
        while people:
            print(people.popleft())
    else:
        people.append(line)