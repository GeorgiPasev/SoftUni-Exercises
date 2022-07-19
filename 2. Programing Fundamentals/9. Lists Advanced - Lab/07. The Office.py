list_of_happiness = input().split()
factor = int(input())

mapping = list(map(lambda x: int(x) * factor, list_of_happiness))

average_happiness = sum(mapping) / len(mapping)
filtered = list(filter(lambda x: x >= average_happiness, mapping))

score = len(filtered)
total_count = len(mapping)
if score >= total_count / 2:
    print(f"Score: {score}/{total_count}. Employees are happy!")
else:
    print(f"Score: {score}/{total_count}. Employees are not happy!")