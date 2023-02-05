tail = input()
body = input()
head = input()

# correct_orientation = [head, body, tail]
correct_orientation = [tail, body, head]
correct_orientation[0], correct_orientation[-1] = correct_orientation[-1], correct_orientation[0]

print(correct_orientation)